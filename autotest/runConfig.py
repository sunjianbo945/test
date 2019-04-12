import os
import subprocess
import filecmp
import sys

import yaml
import difflib
import glob

GOLDEN_DIR = '/usr/local/golden/'
TEST_DIR = '/usr/local/test/'


class OutputTestFile:

    def __init__(self, file_number, file_type, file_name):
        self.file_number = file_number
        self.file_type = file_type
        self.file_name = file_name


class Test:
    def __init__(self,test_id, test_section_name, binary, args, output_files):

        self.test_id = test_id
        self.test_section_name = test_section_name
        self.binary = binary
        self.args = args
        self.output_files = output_files


def compare_with_golden(test):
    command_golden_dir = test.binary + test.args.replace(" ", "")

    for output_file in test.output_files:
        absolute_golden_file_path = os.path.join(os.path.join(GOLDEN_DIR, command_golden_dir), output_file.file_name)
        absolute_test_file_path = os.path.join(TEST_DIR, output_file.file_name)

        bool = filecmp.cmp(absolute_golden_file_path, absolute_test_file_path, shallow=True)
        if not bool:
            print('section => {}, test => {}, file_type => {}, test failed'.format(test.test_section_name, test.test_id,output_file.file_type))

            if output_file.file_type != 'binary':
                file1 = open(absolute_golden_file_path, 'r')
                file1_content = file1.readlines()
                file2 = open(absolute_test_file_path, 'r')
                file2_content = file2.readlines()
                diff = difflib.ndiff(file1_content, file2_content)

                for l in diff:
                    print(l)

                file2.close()
                file1.close()


def read_command(command, section_name, path):

    command = command.strip()
    if len(command) == 0 or command[0] == '#':
        return None

    test_id = command.split(',')[0]
    real_command_line = command.split(',')[1].strip()

    binary = real_command_line.split(' ')[0]

    args = real_command_line[len(binary):]

    output_files=[]

    for output in command.split(',')[2:]:
        temp = output.split('=')[0]
        file_id = temp.split(':')[0]
        file_type = temp.split(':')[1] if len(temp.split(':')) > 1 else 'binary'
        output_file_name = output.split('=')[-1]
        file = OutputTestFile( file_id, file_type,output_file_name)
        output_files.append(file)

    # copyfile(absolute_binary_path,TEST_DIR)
    linux_command = 'rm -rf ' + TEST_DIR + "*"

    subprocess.call(linux_command,shell=True)
    if path is not None:
        linux_command = "cp " + os.path.join(path, binary) + ' '+ TEST_DIR
    else:
        linux_command = "cp " + os.path.join('.',binary) + ' ' + TEST_DIR

    subprocess.call(linux_command,shell=True)
    return Test(test_id, section_name, binary, args, output_files)


def main():
    '''
    1.  Under current directory, looking for .conf file
    2.  Read all lines of the .conf file
    3.  Run binary assume that under current/test/debug/bin
    4.  Compare the output under current/test/debug/bin/ vs current/binary/
    :return:
    '''

    # get all .conf files under current directory

    dir = sys.argv[1]
    files = glob.glob(dir+'/*test.yaml')

    for file in files:
        with open(file, 'r') as f:
            doc = yaml.load(f,Loader=yaml.FullLoader )
            for section in doc['regression-test']:
                for test in section['test-section']['tests']:
                    test_section = read_command(test, section['test-section']['name'], section['test-section']['path'])
                    run_command = './' + test_section.binary + test_section.args
                    os.chdir(TEST_DIR)
                    os.system(run_command)
                    compare_with_golden(test_section)


if __name__ == '__main__':
    main()




