import random # import random module to use choice() method
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Requires opencv-python
import numpy as np
import time
from contextlib import contextmanager

class RPS:
    '''
    This class represents an instance of the computer vision rock-paper-scissors game.

    Attributes:
        computer_wins: integer representing the number of rounds the computer has won
        user_wins: integer representing the number of rounds the user has won
        cap: opencv VideoCapture class, used for capturing images from computer webcam
        image: image captured from webcam using VideoCapture read() method
        game_started: boolean representing the status of the game
        timer: integer used for counting down each round of the game
        model: keras machine learning model class
        class_names: list representation of machine learning model class labels
    '''
    def __init__(self):
        '''Initialises an instance of the RPS class'''
        self.computer_wins = 0
        self.user_wins = 0
        self.cap = cv2.VideoCapture(0)
        self.image = []
        self.game_started = False
        self.timer = 0
        self.model = load_model("keras_model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()

        
    def get_computer_choice(self):
        '''Returns a random choice as a string - either 'rock', 'paper', or 'scissors'.'''
        # use random.choice() to randomly select and return one of the strings
        return random.choice(['rock', 'paper', 'scissors'])


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
        # print the user and computer choices to the terminal
        print(f"\nYou chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        # check if user didn't make gesture
        if user_choice == 'nothing':
            print("No gesture was detected, round is null")
            return "nothing"
        # check all three conditions whereby computer can win
        elif (computer_choice == 'rock' and user_choice == 'scissors') or \
        (computer_choice == 'paper' and user_choice == 'rock') or \
        (computer_choice == 'scissors' and user_choice == 'paper'):
            # if any of these are met, print losing message to console and return winner as string
            print("You lost this round")
            return "computer"
        # check if user_choice and computer_choice are identical
        elif computer_choice == user_choice:
            # if so, print tie message to console and return 'tie' as string
            print("This round was a tie!")
            return "tie"
        else:
            # otherwise, print winning message to console and return winner as string
            print("You won this round!")
            return "user"


    @contextmanager
    def get_video(self):
        '''
        Shows the video image from the computer webcam.

        Uses the cv2 VideoCapture class method read() to generate an image from webcam video, then flips and crops the image.
        Utilises @contextmanager decorator to enable this function to wrap other lines of code.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # Grab the webcamera's image.
        ret, image = self.cap.read()
        # Flip the image along the vertical axis as most people are used to seeing mirror image
        self.image = cv2.flip(image,1)
        # crop image to roughly match the capture area from Teachable Machine
        self.image = self.image[:, 300:-300]
        # try any code accompanying this function in with statement
        try:
            yield
        finally:
            # Show the image in a window
            cv2.imshow("Webcam Image", self.image)

    
    def get_prediction(self):
        '''
        Returns a prediction of user gesture in image based on machine learning model.

        Takes the class attribute image (generated from webcam), resizes it to match ML model, turns it into a numpy array
        and normalises it before predicting which gesture the user made and returning the prediction.

        Parameters
        ----------
        None

        Returns
        -------
        class_name: str
            string representing the classname predicted from the ML model
        '''
        # Resize the raw image into (224-height,224-width) pixels
        gesture = cv2.resize(self.image, (224, 224), interpolation=cv2.INTER_AREA)
        # Make the image a numpy array and reshape it to the models input shape.
        gesture = np.asarray(gesture, dtype=np.float32).reshape(1, 224, 224, 3)
        # Normalise the image array
        gesture = (gesture / 127.5) - 1
        # Predict the gesture using the model
        prediction = self.model.predict(gesture, verbose=0)
        # Get the index of the class with the highest prediction score
        index = np.argmax(prediction)
        # Use the index to get the string representation of that class
        class_name = self.class_names[index]
        # Return a sliced version of the string removing the class number and trailing newline, and converting to lowercase
        return class_name[2:-1].lower()


    def put_text_intro(self):
            '''Uses cv2.putText() to place a series of messages on the screen at various positions'''
            cv2.putText(self.image, "Rock, Paper, Scissors!", (100, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "Show your gesture to the webcam.", (50, 200), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "When the countdown ends, your", (50, 250), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "choice is captured and the round", (50, 300), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "winner is declared in the terminal.", (50, 350), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "Press 'q' between rounds to quit.", (50, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)
            cv2.putText(self.image, "Press 'c' to continue...", (50, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)


    def display_prompt(self):
        '''Displays either the game intro screen or the continue prompt depending on whether the game has started or not.'''
         # check if the game has started
        if self.game_started == False:
            # if not, display the intro text to the screen
            with self.get_video():
                self.put_text_intro()
        # if the game has started, display the continue prompt
        else:
            with self.get_video():
                cv2.putText(self.image, "Press 'c' to continue...", (50, 400), cv2.FONT_HERSHEY_DUPLEX, 1, (21, 35, 189), 2, cv2.LINE_AA)


    def play_round(self):
        '''
        Plays a round of rock-paper-scissors.

        Displays a countdown timer to the screen - when the timer reaches zero, an image is captured and the user's gesture
        is predicted. A random computer gesture is generated and the two are compared. A round winner is declared based on
        the rules of the game and the class attributes are updated to keep score for the game overall. Round result and 
        current game score are displayed in the terminal.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # set the timer length
        self.timer = 5
        # get the time now for starting the timer
        prev_time = time.time()
        # loop while timer is running
        while self.timer > 0:
            # get the current time
            curr_time = time.time()
            # compare the time now to the time when the round started, if more than one second has elapsed...
            if curr_time - prev_time >= 1:
                # reset the previous time
                prev_time = curr_time
                # decrease timer by one
                self.timer -= 1
            # start the video and write the timer to the screen
            with self.get_video():
                cv2.putText(self.image, str(self.timer), (300, 300), cv2.FONT_HERSHEY_DUPLEX, 4, (21, 35, 189), 4, cv2.LINE_AA)
                cv2.waitKey(1) # wait for input needed to keep video open
        # once the timer reaches zero get a new video image without text
        with self.get_video():
            # call the functions to get computer choice and prediction of user gesture, compare to find the winner
            # and assign to result.
            result = self.get_winner(self.get_computer_choice(), self.get_prediction())
            # update class attributes based on the result
            if result == 'computer':
                self.computer_wins += 1
            elif result == 'user':
                self.user_wins += 1
            # print current game score to terminal
            print(f"Current score: Computer: {self.computer_wins} | User: {self.user_wins}")


    def play(self):
        '''
        Enables user to play a full game of rock-paper-scissors against the computer.

        Loops over successive rounds of the game, calling the necessary functions until one of the players has reached
        three wins (i.e. best of five rounds).

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        # set up loop that ends once either player reaches three wins
        while self.computer_wins < 3 and self.user_wins < 3:
            # display prompt
            self.display_prompt()
            # wait for user input...
            keystroke = cv2.waitKey(1)
            # check user input - if user presses 'c'...
            if keystroke == ord('c'):
                # start the game
                self.game_started = True
                # play a round
                self.play_round()
            # otherwise, game can be ended at any time by pressing 'q' key
            elif keystroke == ord('q'):
                break
        # check which player reached three wins first and display winner to the terminal
        if self.computer_wins == 3:
            print("\nThe computer won the game\n")
        elif self.user_wins == 3:
            print("\nYou won the game!\n")
        else:
            print("\nYou ended the game before three round wins were achieved.\n")
        # clean up the video capture object and close the image window
        self.cap.release()
        cv2.destroyAllWindows()

game = RPS()
game.play()