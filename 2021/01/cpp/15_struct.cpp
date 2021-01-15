//small demonstration of struct (user defined data type just like an array but can hold heterogeneous data in one data block)

#include<iostream>

using namespace std;

struct students
{
	string name;
	float GPA;
};

int main()
{
	students grade12[10];
	grade12[0].name = 'Andy';
	grade12[1].name = 'Sam';
	grade12[0].GPA = 3.2;

	cout << grade12[0].name << endl;

	return 0;
}