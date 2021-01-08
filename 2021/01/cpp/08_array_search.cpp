//program to linearly search the array and return the index of the element inserted.

#include<iostream>

using namespace std;

int searchNum(int arr[], int len, int num);

int main()
{
	int numWant = 0;

	int arr[] = {2,25,1,49,21,47,23,19,89};

	int length = sizeof(arr)/sizeof(arr[0]);

	int i = 0;

	//printing the array
	while(i < length)
	{
		cout << arr[i] << " ";
		i++;
	}

	cout << "Enter the number you want index of from the array: ";

	cin >> numWant;

	int position = searchNum(arr, length, numWant);

	if (position == -1)
		cout << "Element not found!";
	else
		cout << "Element found at index " << position+1;

	return 0;
}

//function that does the linear search in the array 
int searchNum(int arr[], int len, int num)
{

	for(int i = 0; i < len; i++)
	{
		if(arr[i] == num)
			return i;
	}
	return -1;
}