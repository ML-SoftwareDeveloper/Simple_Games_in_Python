import random

# Get player's name
player_name = input('Please enter your name:')

# Print welcome message
print('Hello',player_name,'!, Lets begin...')

# Available choices
choices = ['R','S','P']

def decide(player_choice,computer_choice):
    if player_choice==computer_choice:
        return 'tie'
    elif choices.index(player_choice)+1==choices.index(computer_choice) or choices.index(player_choice)-choices.index(computer_choice)==2:
        return 'Congrats! You won :)'
    else:
        return 'Unlucky! Computer won :('

def rps():
    check_tie = False #Flag

    # Play until its not a tie
    while not check_tie:
        # Get players choise
        player_choice = input('Choose R(rock) or P(paper) or S(scissor): ') 
        print('Your choise:',player_choice)
        # If user does invalid selection
        while player_choice not in choices:
            print('Please make a valid choise !')
            player_choice = input('Choose R(rock) or P(paper) or S(scissor): ')
        # Get computers choise
        computer_choice = random.choice(choices)
        print("Computer's choice:",computer_choice)
        decision = decide(player_choice,computer_choice)
        if decision=='tie':
            print('Its a tie :| Try again !')
        else:
            check_tie = True
    print(decision)
    
    # Play again?
    again = input('Play again y or n ?: ')
    if again=='y':
        rps()
    elif again=='n':
        print('Goodbye!')
        pass
    else:
        print('Invalid choice, Goodbye!')
        return 0

# Call function
rps()












