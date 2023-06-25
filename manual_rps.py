import random # import random module to use choice() method

def get_computer_choice():
    '''Returns a random choice - either 'rock', 'paper', or 'scissors'.'''
    # use random.choice() to randomly select and return one of the strings
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    '''
    Returns user choice of either Rock, Paper, or Scissors.
    
    Takes user input and checks that it is valid. Will repeatedly ask for input if user does not input 'Rock', 'paper' or 'scissors'.
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

# call functions to test
print(get_computer_choice())
print(get_user_choice())

