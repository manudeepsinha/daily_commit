#include<iostream>

using namespace std;

int fib(int num);

int main()
{
	int userInput = 0;

	cout << "Enter a index number of fibonacci number which you want : ";

	cin >> userInput;

	fib(userInput);

	return 0;
}

int fib(int num)
{
	if (num <= 1)
		return num;

	return fib(num-1) + fib(num-2);
}




//Fibonacci Series using Recursion 
#include<bits/stdc++.h> 
using namespace std; 

int fib(int n) 
{ 
	if (n <= 1) 
		return n; 
	return fib(n-1) + fib(n-2); 
} 

int main () 
{ 
	int n = 9; 
	cout << fib(n); 
	return 0; 
} 

// This code is contributed 
// by Akanksha Rai 
