//This is the second code, refactored with various functions for better readability and performance.

/*The following code is for the game of chips for two players.
The game begins with a number of chips in the pile.
Each player then takes a number of allowed chips to be taken per round.
Whoever takes the last chips looses the game.
*/
#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

const float MAX_TURN = 0.5;
const int MAX_CHIPS = 100;

string FindPlayerName (string names[2], bool playerTurn);
void GetUserNames (string players[2]);
int AskMove (bool player1Turn, int chipsInPile, string names[]);

int main()
{

	int chipsInPile = 0;
	int chipsTaken = 0;

	char userChoice;

	bool player1Turn = true;
	bool gameOver = false;

	string playerNames[2];

	//seeding the random number generator
	srand(time(0));

	//taking input of names and storing in an array
	GetUserNames(playerNames);

	do
	{
		//assigning number of chips in the pile
		chipsInPile = (rand() % MAX_CHIPS) + 1;
		cout << "This round will start with " << chipsInPile << " chips.";
		gameOver = false;
		
		while (gameOver == false)
		{
			chipsTaken = AskMove(player1Turn, chipsInPile, playerNames);
			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " chips left in the pile.";
			player1Turn = !player1Turn;
			//when the game is over. Now determining the winner
			if(chipsInPile == 0)
			{
				gameOver = true;

				cout << FindPlayerName(playerNames, player1Turn) << ", congratulations you won\n";

			}
		}
			//asking to play again or not
			cout << "Do you want to play again? (Y/N): ";
			cin >> userChoice;
			userChoice = toupper(userChoice);

	} while (userChoice == 'Y');

	return 0;
}


////////////////////FUNCTIONS////////////////////FUNCTIONS////////////////////FUNCTIONS////////////////////

//determining the name of the player to display
string FindPlayerName (string names[], bool playerTurn)
{
	if (playerTurn)
		return names[0];

	else
		return names[1];
}


//taking player names and storing them in an array
void GetUserNames (string players[])
{
	cout << "Player 1 please enter your name: ";
	cin >> players[0];
	cout << "\nThank you and good luck!" << endl << "Player 2 please enter your name: \n(If you wish to play against computer, enter AI)";
	cin >> players[1];
	cout << "\nThank you and good luck!";
}


//this will ask the player to take certain number of chips and then the game proceeds
int AskMove (bool player1Turn, int chipsInPile, string names[])
{
	int chipsTaken;
	int maxPerTurn = chipsInPile * MAX_TURN;
	do
	{
		//loop checks that the player takes valid number of chips

		cout << FindPlayerName(names, player1Turn) << " how many chips will you take?";

		cout << "You can take upto: ";

		if(maxPerTurn == 0)
		{
			cout << "1\n";
		}
		else
		{
			cout << maxPerTurn << endl;
		}

		if (FindPlayerName(names, player1Turn) == "AI")
		{
			if (maxPerTurn == 0)
				chipsTaken = 1;

			else
				chipsTaken = (rand() % maxPerTurn) + 1;
		}

		else
			cin >> chipsTaken ;

	} while((chipsTaken > maxPerTurn) && (chipsInPile > 1));

	return chipsTaken;
}
