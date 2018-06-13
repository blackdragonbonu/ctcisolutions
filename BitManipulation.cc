/*
For bit manipulation questions we need to use  a faster language hence we are planning to c++. Also due to python lacking the inherent support for bit manipulation.
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
We are asked to get two integers. The first integer is larger than the second. And we make a certain part of first integer the same as the second iteger.and then we take the indexes where the element has to be replaced.
*/


int  main(){
	string strinput;
	vector <bool> bit_array;
	int bit_int,smaller_int=0,index;
	
	cout<<"Enter a string that needs to be made into a bit array \n";
	cin>>strinput;
	for (size_t i=0;i<strinput.size();i++){
		bit_array.push_back(strinput[i]=='1');
		cout<<bit_array[i];
		bit_int |=bit_array[i]<<i;
	}
	cout<<"\n";
	cout<<bit_int<<endl;
	cout<<"Enter the second striing that needs to be made into a bit array\n";
	cin>>strinput;
	for (size_t i=0;i<strinput.size();i++){
		bool bit=strinput[i]=='1';
		smaller_int|=bit<<i;
	}
	cout<<"Enter the index where you want to insert the bit";
	cin>>index;
		

}





