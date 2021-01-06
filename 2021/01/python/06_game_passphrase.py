#Have to check why the passphrase's length is showing +1 by default
#You've to guess the passphrase to win this game
#it's a basic construct and will develop over it in the near future.
file = open("04_game_passphrase.txt", 'r')

for passphrase in file:
    print(f'The passphrase is: {passphrase}')
    userGuess = int(input('Enter your guess for pass patern in integer\n'))
    
    if userGuess == (len(passphrase) - 1):
        print('Congratulations! You have guessed it right!\n')
    else:
        print('Better luck next time!\n')
print(input(('\nDid you enjoy the game?')))