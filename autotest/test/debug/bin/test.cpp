#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void write_line(string fileName){
    std::ofstream out(fileName);
    out << "This is the golden copy of the binary \"testbinary\"";
    out.close();
}


int main(int argc, char *argv[]){

    for(int i =1;i<argc; i++){
        write_line(argv[i]);
    }

}