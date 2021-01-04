/*more comments and adding of code and fun is pending. work in progress.
Will upload the later version later.
*/

#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream inStream;
	int userGuess = 0;

	inStream.open("04_game_passphrase.txt");

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
				cout << "Sorry try again later!\n";
		}
		
	}
	inStream.close();
	return 0;
}