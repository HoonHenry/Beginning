//#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	int num = 3;
	int *pNum = &num; //the address of the pNum is pointing to, pointer should assign the address
	cout << pNum << endl; //the address of the pNum
	cout << *pNum << endl; //the assigned value at the address of pNum pointing to

	*pNum = 45;	//update the value 3 -> 45, the num will be also updating the value 3 -> 45
	cout << *pNum << endl;
	cout << num << endl;

	return 0;
}