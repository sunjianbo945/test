#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void write_line(string fileName,int flag){
    std::ofstream out(fileName);
    if(flag == 1){
    	out << "flag 1 "<<fileName;
    }else{
        out << "flag 2 "<<fileName;  
    }
    out.close();
}


int main(int argc, char *argv[]){
//	cout<<argv[1]<<endl;
    if(argv[1][8]=='1'){
    	write_line("happy.out",1);
        write_line("sad.out",1);
    }else{
	write_line("happy.out",2);
	write_line("sad.out",2);
    }

}
