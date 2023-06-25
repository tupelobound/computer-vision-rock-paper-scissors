import random # import random module to use choice() method
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Requires opencv-python
import numpy as np
import time
import math

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

class RPS:
    '''
    This class represents an instance of the computer vision rock-paper-scissors game.

    '''
    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0

        
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

    """
    def get_prediction(self):
        '''
        Uses the camera to acquire image of user presenting gesture and then makes prediction of what the gesture is based
        on the model trained on Teachable Machine.
        '''
        # Load the model
        model = load_model("keras_Model.h5", compile=False)

        # Load the labels
        class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        camera = cv2.VideoCapture(0)

        while True:
            # Grab the webcamera's image.
            ret, image = camera.read()

            # Resize the raw image into (224-height,224-width) pixels
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

            # Show the image in a window
            cv2.imshow("Webcam Image", image)

            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

            # Predicts the model
            prediction = model.predict(image)
            index = np.argmax(prediction)
            class_name = class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(1)

            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break

        camera.release()
        cv2.destroyAllWindows()
        return prediction"""


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

game = RPS()
game.play()