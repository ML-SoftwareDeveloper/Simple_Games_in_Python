import random

# Get player's name
player_name = input('Please enter your name:')

# Print welcome message
print('Hello',player_name,'!, Lets begin...')

# Available choices
choices = ['R','S','P']


def decide(player_choice,computer_choice):
    if player_choice==computer_choice:
        print('Its a tie. Try again !')
        main()
    elif choices.index(player_choice)+1==choices.index(computer_choice) or choices.index(player_choice)-choices.index(computer_choice)==2:
        return 'Congrats! You won :)'
    else:
        return 'Unlucky! Computer won :('




def main():
    # Get players choise
    player_choice = input('Choose R(rock) or P(paper) or S(scissor)')
    print('Your choise:',player_choice)
    if player_choice not in choices:
        print('Please make a valid choise !')
        main()

    # Get computers choise
    computer_choice = random.choice(choices)
    print("Computer's choice:",computer_choice)

    decision = decide(player_choice,computer_choice)

    print(decision)

    again = input('Play again y or n ?')

    if again=='y':
        main()
    else:
        print('Goodbye!')



main()












