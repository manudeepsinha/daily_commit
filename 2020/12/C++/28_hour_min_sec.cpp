/*This code will print each hour, minute, and second in a day. It demonstrates how nested for loop impact 
on the performance of the code when iterating over large amount of data.
*/
#include<iostream>
#include<ctime>
#include<cstdlib>
using namespace std;

int main()
{
	for (int hour = 0; hour < 24; hour++){
		for (int minute = 0; minute < 60; minute++){
			for (int second = 0; second < 60; second++){
				cout<<hour<<":"<<minute<<":"<<second<<endl;
			}

		}

	}
	return 0;
}
