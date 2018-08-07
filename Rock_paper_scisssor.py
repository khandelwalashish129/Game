name_1 = input('Player 1 what is your name: ')

name_2 = input('Player 2 what is your name: ')

while True:

    player_1 = input((name_1) + ', please choose Rock, Paper or Scissors (r/p/s): ')

    player_2 = input((name_2) + ', please choose Rock, Paper or Scissors (r/p/s): ')

    if player_1 == 'r' and player_2 == 's' or player_1 == 'p' and player_2 == 'r' or player_1 == 's' and player_2 == 'p':

        print(name_1 + ' wins!')

    elif player_2 == 'r' and player_1 == 's' or player_2 == 'p' and player_1 == 'r' or player_2 == 's' and player_1 == 'p':

        print(name_2 + ' wins!')

    elif player_2 == 'r' and player_1 == 'r' or player_2 == 'p' and player_1 == 'p' or player_2 == 's' and player_1 == 's':

        print('Tie')

    else:

        print('Error! Please type p for Paper, s for Scissors or r for Rock')

    if input('Do you want to start a new game? Type yes or no (y/n): ') == 'n':
        break
print('goodbye')

