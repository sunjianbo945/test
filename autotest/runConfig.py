import shlex
import os
import difflib
import subprocess
from shutil import copyfile
import filecmp

GOLDEN_DIR = '/usr/local/golden/'
TEST_DIR = '/usr/local/test/'

def run_command(command):
    command = command.strip()

    command_info = command.split(',')
    binary_loc = command_info[0].split(' ')[0]
    copyfile(binary_loc, TEST_DIR)
    binary = binary_loc.split('/')[-1]

    run_command = TEST_DIR+binary+' '+command_info[0].split(' ')[1:]

    subprocess.run(run_command)


def compare_with_golden(line):
    pass




def main():
    '''
    1.  Under current directory, looking for .conf file
    2.  Read all lines of the .conf file
    3.  Run binary assume that under current/test/debug/bin
    4.  Compare the output under current/test/debug/bin/ vs current/binary/
    :return:
    '''

    # get all .conf files under current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f) and '.conf' in f]
    for file in files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                run_command(line)
                compare_with_golden(line)


if __name__ == '__main__':
    main()




