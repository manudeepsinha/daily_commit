/*what's new: moves counter
			  winner name written in output file.
			  struct that saves player wins per round*/

/*The following code is for the game of chips for two players.
The game begins with a number of chips in the pile.
Each player then takes a number of allowed chips to be taken per round.
Whoever takes the last chips looses the game.
*/
#include<iostream>
#include<ctime>
#include<cstdlib>
#include<fstream>

using namespace std;

struct player
{
	string name;
	int win;	
};

const float MAX_TURN = 0.5;
const int MAX_CHIPS = 100;

string FindPlayerName (player[], bool playerTurn);
void GetUserNames (player[]);
int AskMove (bool player1Turn, int chipsInPile, player[]);
void AddWins (player[], bool player1Turn);

int main()
{

	int chipsInPile = 0;
	int chipsTaken = 0;
	int moves = 0;

	char userChoice;

	bool player1Turn = true;
	bool gameOver = false;

	player Players[2];

	ofstream outStream;
	outStream.open("Winner.txt", ios::app);

	//seeding the random number generator
	srand(time(0));

	//taking input of names and storing in an array
	GetUserNames(Players);

	do
	{
		//assigning number of chips in the pile
		chipsInPile = (rand() % MAX_CHIPS) + 1;
		cout << "This round will start with " << chipsInPile << " chips.";
		gameOver = false;
		moves = 0;
		
		while (gameOver == false)
		{
			chipsTaken = AskMove(player1Turn, chipsInPile, Players);
			chipsInPile = chipsInPile - chipsTaken;
			cout << "There are " << chipsInPile << " chips left in the pile.";
			player1Turn = !player1Turn;
			moves++ ;
			//when the game is over. Now determining the winner
			if(chipsInPile == 0)
			{
				gameOver = true;

				cout << FindPlayerName(Players, player1Turn) << ", congratulations you won\n";
				outStream << FindPlayerName(Players, player1Turn) << "has won in " << moves << " chances." << endl;
				AddWins(Players, player1Turn);

			}
		}
			//asking to play again or not
			cout << "Do you want to play again? (Y/N): ";
			cin >> userChoice;
			userChoice = toupper(userChoice);

	} while (userChoice == 'Y');
	cout << Players[0].name << " had won " << Players[0].win << " times this round." << endl;
	cout << Players[1].name << " had won " << Players[1].win << " times this round." << endl;
	outStream.close();

	return 0;
}


////////////////////FUNCTIONS////////////////////FUNCTIONS////////////////////FUNCTIONS////////////////////

//determining the name of the player to display
string FindPlayerName (player Players[], bool playerTurn)
{
	if (playerTurn)
		return Players[0].name;

	else
		return Players[1].name;
}


//taking player names and storing them in an array
void GetUserNames (player Players[])
{
	cout << "Player 1 please enter your name: ";
	cin >> Players[0].name;
	cout << "\nThank you and good luck!" << endl << "Player 2 please enter your name: \n(If you wish to play against computer, enter AI)";
	cin >> Players[1].name;
	cout << "\nThank you and good luck!";
	Players[0].win = 0;
	Players[1].win = 0;
}


//this will ask the player to take certain number of chips and then the game proceeds
int AskMove (bool player1Turn, int chipsInPile, player Players[])
{
	int chipsTaken;
	int maxPerTurn = chipsInPile * MAX_TURN;
	do
	{
		//loop checks that the player takes valid number of chips

		cout << FindPlayerName(Players, player1Turn) << " how many chips will you take?";

		cout << "You can take upto: ";

		if(maxPerTurn == 0)
		{
			cout << "1\n";
		}
		else
		{
			cout << maxPerTurn << endl;
		}

		if (FindPlayerName(Players, player1Turn) == "AI")
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

void AddWins (player Players[], bool player1Turn)
{
	if (player1Turn)
		Players[0].win++;
	
	else
		Players[1].win++;
}
