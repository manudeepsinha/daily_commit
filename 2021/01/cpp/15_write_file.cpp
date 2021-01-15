#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream inStream;  //used to declare input file reader -> ifstream
	ofstream outStream; //used to declare input file writer -> ofstream

	int userGuess = 0;

	inStream.open("passPhrase.txt");
	outStream.open("newPassPhrase.txt");
	// if the file already exists, write ios::app after the name of the file in braces, eg: ('newPassPhrase.txt', ios::app);
	string passPhrase;

	if (!inStream.fail())
	{
		while (inStream >> passPhrase)
		{
			cout << "The pass phrase is: " << passPhrase << endl;

			cout << "What is your guess?" << endl;
			cin >> userGuess;

			if (userGuess == passPhrase.length())
			{
				cout << "Congrats\n";
			}
			else
			{
				cout << "Sorry try again later!\n";
				outStream << passPhrase << endl;
			}
		}
		
	}
	inStream.close();
	outStream.close();
	return 0;
}