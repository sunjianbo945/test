//============================================================================
// Name        : sqlogd.cpp
// Author      : JIanbo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <ctime>
#include <thread>
#include <chrono>
using namespace std;


int main() {

	std::ofstream outfile;

	outfile.open("test.txt", std::ios_base::app);

	int sleepTime = 5;
	for(int i =0;i<24*60*10;i++){
		time_t rawtime;
		struct tm * timeinfo;
		char buffer[80];

		time (&rawtime);
		timeinfo = localtime(&rawtime);

		strftime(buffer,sizeof(buffer),"%d-%m-%Y %H:%M:%S",timeinfo);
		std::string str(buffer);

		outfile<<str<<endl;

		std::this_thread::sleep_for(std::chrono::milliseconds(sleepTime*1000));

	}
	outfile.close();
	cout << "!!!Hello World test done!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
