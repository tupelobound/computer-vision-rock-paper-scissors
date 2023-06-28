import random # import random module to use choice() method
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Requires opencv-python
import numpy as np
import time
import math
from contextlib import contextmanager

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

class RPS:
    '''
    This class represents an instance of the computer vision rock-paper-scissors game.

    Attributes:
        computer_wins: integer representing the number of rounds the computer has won
        user_wins: integer representing the number of rounds the user has won
    '''
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.cap = cv2.VideoCapture(0)
        self.image = []
        self.game_started = False
        self.timer = 0
        self.model = load_model("keras_model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()

        
    def get_computer_choice(self):
        '''Returns a random choice - either 'rock', 'paper', or 'scissors'.'''
        # use random.choice() to randomly select and return one of the strings
        return random.choice(['rock', 'paper', 'scissors'])


    def get_user_choice(self):
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


    def get_winner(self, computer_choice, user_choice):
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
        result : str
            A string representing the winner - either the user or the computer, or a tie
        '''
        # check all three conditions whereby computer can win
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        print("------------------------------------")
        if (computer_choice == 'rock' and user_choice == 'scissors') or \
        (computer_choice == 'paper' and user_choice == 'rock') or \
        (computer_choice == 'scissors' and user_choice == 'paper'):
            # if so, print losing message to console
            print("\nYou lost this round")
            return "computer"
        # check if user_choice and computer_choice are identical
        elif computer_choice == user_choice:
            # if so, print tie message to console
            print("\nThis round was a tie!")
            return "tie"
        else:
            # otherwise, print winning message to console
            print("\nYou won this round!")
            return "user"


    @contextmanager
    def get_video(self):
        # Grab the webcamera's image.
        ret, image = self.cap.read()
        # Flip the image along the vertical axis as most people are used to seeing mirror image
        self.image = cv2.flip(image,1)
        # crop image to roughly match the capture area from Teachable Machine
        self.image = self.image[:, 300:-300]
        try:
            yield
        finally:
            # Show the image in a window
            cv2.imshow("Webcam Image", self.image)

    
    def get_prediction(self):
        # Resize the raw image into (224-height,224-width) pixels
        gesture = cv2.resize(self.image, (224, 224), interpolation=cv2.INTER_AREA)
        # Make the image a numpy array and reshape it to the models input shape.
        gesture = np.asarray(gesture, dtype=np.float32).reshape(1, 224, 224, 3)
        # Normalize the image array
        gesture = (gesture / 127.5) - 1
        # Predicts the model
        prediction = self.model.predict(gesture)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        return class_name[2:-1].lower()


    def countdown(self):
        '''Runs a simple countdown timer.'''
        # set start time
        start_time = time.time()
        # set time now
        now = time.time()
        # set an integer value for the seconds since start of function call
        old_seconds_since_start = math.floor(now - start_time)
        # run loop only while less than seven seconds have elapsed from start time
        while now < start_time + 7:
            # set a new value for seconds since start time
            new_seconds_since_start = math.floor(now - start_time)
            # check if floor integer of new seconds since start is different to floor integer value of old seconds since start
            if old_seconds_since_start != new_seconds_since_start:
                # if so, print value starting at 5
                print(5 - old_seconds_since_start)
            # update value of time now
            now = time.time()
            # change old seconds since start to new seconds since start
            old_seconds_since_start = new_seconds_since_start


    def play(self):
        while self.computer_wins < 3 and self.user_wins < 3:
            result = self.get_winner(self.get_computer_choice(), self.get_user_choice())
            if result == 'computer':
                self.computer_wins += 1
            elif result == 'user':
                self.user_wins += 1
            print(f"Current score: Computer: {self.computer_wins} | User: {self.user_wins}\n")
        if self.computer_wins == 3:
            print("The computer won the game")
        elif self.user_wins == 3:
            print("You won the game!")

        
    def test(self):
        while True:
            if self.game_started == False:
                with self.get_video():
                    cv2.putText(self.image, "Rock, Paper, Scissors!", (100, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                    cv2.putText(self.image, "Show your gesture to the webcam.", (50, 200), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                    cv2.putText(self.image, "When the countdown ends, your", (50, 250), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                    cv2.putText(self.image, "choice is captured and the round", (50, 300), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                    cv2.putText(self.image, "winner is declared in the terminal.", (50, 350), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                    cv2.putText(self.image, "Press 'c' to continue...", (50, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            else:
                with self.get_video():
                    cv2.putText(self.image, "Press 'c' to continue...", (50, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            
            keystroke = cv2.waitKey(1)
            
            if keystroke == ord('c'):
                self.game_started = True
                self.timer = 5
                prev_time = time.time()
                while self.timer > 0:
                    curr_time = time.time()
                    if curr_time - prev_time >= 1:
                        prev_time = curr_time
                        self.timer -= 1
                    with self.get_video():
                        cv2.putText(self.image, str(self.timer), (50, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
                        cv2.waitKey(1)
                with self.get_video():
                    self.get_winner(self.get_computer_choice(), self.get_prediction())
            elif keystroke == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
    

game = RPS()
game.test()
print(game.class_names)