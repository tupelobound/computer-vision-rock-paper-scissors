import random # import random module to use choice() method

def get_computer_choice():
    '''Returns a random choice - either 'rock', 'paper', or 'scissors'.'''
    # use random.choice() to randomly select and return one of the strings
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    '''
    Returns user choice of either 'rock', 'paper', or 'scissors'.

    Takes user input and checks that it is valid. Will repeatedly ask for input if user does not input 'rock', 'paper' or 'scissors'.
    Converts user input to lowercase, so capitalization is fine.
    '''
    # ask user to input their choice and convert to lowercase
    user_choice = input("Please enter your choice of rock, paper or scissors: ").lower()
    # start loop
    while True:
        # check if user input is valid
        if user_choice in ['rock', 'paper', 'scissors']:
            # if so, end loop and return user_choice
            return user_choice
        else:
            # otherwise, ask for input again and convert to lowercase
            user_choice = input("Sorry, that isn't a valid input. Please enter either rock, paper or scissors: ").lower()

def get_winner(computer_choice, user_choice):
    '''
    Takes two strings, compares them and evaluates who the winner is based on the rules of rock-paper-scissors.

    Parameters
    ----------
    computer_choice : str
        A string generated from running the function get_computer_choice
    user_choice : str
        A string generated from running the function get_user_choice
        
    Returns
    -------
    None
    '''
    # check all three conditions whereby computer can win
    if (computer_choice == 'rock' and user_choice == 'scissors') or \
       (computer_choice == 'paper' and user_choice == 'rock') or \
       (computer_choice == 'scissors' and user_choice == 'paper'):
        # if so, print losing message to console
        print("You lost")
    # check if user_choice and computer_choice are identical
    elif computer_choice == user_choice:
        # if so, print tie message to console
        print("It is a tie!")
    else:
        # otherwise, print winning message to console
        print("You won!")

def play():
    '''Runs one round of the game rock-paper-scissors.'''
    get_winner(get_computer_choice(), get_user_choice())

# run play() function to test code
play()