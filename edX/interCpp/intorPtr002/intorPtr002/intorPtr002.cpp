#include <iostream>
using namespace std;

int main() {
	//declare and initialize an int variable
	int num = 3;

	//create a reference type and assign num to it
	int &refNum = num;

	//output the value contained in num and refNum - they are the same value
	cout << "num contains " << num << endl;
	cout << "refNum contains " << refNum << endl;

	//increment refNum by 1
	refNum++;

	//output the new value of num and refNum - they are the same value
	cout << "num contains " << num << endl;
	cout << "refNum contains " << refNum << endl;

	//increment num by 1
	num++;

	//output the new value of num and refNum - they are the same value
	cout << "num contains " << num << endl;
	cout << "refNum contains " << refNum << endl;

	return 0;
}