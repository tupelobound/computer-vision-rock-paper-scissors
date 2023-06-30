# Computer Vision Rock-Paper-Scissors

This project recreates the classic game Rock-Paper-Scissors, pitting the user against the computer in a best-of-three encounter.
The rules of the game are simple - after a countdown both players present a hand gesture representing one of either Rock, Paper
or Scissors:

![](https://hips.hearstapps.com/hmg-prod/images/people-playing-paper-rock-scissors-royalty-free-illustration-1583269312.jpg?crop=0.994xw:0.799xh;0.00160xw,0.195xh&resize=2048:*)
*Image credit: https://www.popularmechanics.com/culture/gaming/a31213381/rock-paper-scissors-history/*

Rock defeats Scissors, Paper defeats Rock, Scissors defeats Paper. When both players present
the same gesture, the round is a tie.

In a modern twist, the user presents their hand gesture to their computer webcam, the image is captured, computer vision machine 
learning takes over and makes a prediction of which gesture the user presented.

# Project Dependencies

In order to run this project, the following modules need to be installed:

- `opencv-python`
- `tensorflow`
- `ipykernel`

It's recommended that a new virtual environment is created for this project, and the dependencies installed within the virtual
environment. [Conda](https://docs.conda.io/en/latest/) is an excellent solution for creating and managing virtual environments.

To create a new virtual environment in Conda type the following command in the terminal,

`conda create -n $ENVIRONMENT_NAME`

where `$ENVIRONMENT_NAME` is whatever name you choose for the environment. Then run the following command to activate the new
virtual environment:

`conda activate $ENVIRONMENT_NAME`

At the time of writing, you will need to use `pip` to install `opencv-python`:

`conda install pip`

`pip install opencv-python`

Conda can be used to install `tensorflow` and `ipykernel` in your new virtual environment. Run the following in the terminal:

`conda install $PACKAGE_NAME`

Alternatively, the Conda environment can be cloned by running the following command, ensuring that env.yaml is present in the
project:

`conda create env -f env.yaml -n $ENVIRONMENT_NAME`

# Manual version of the game

The file `manual_rps.py` contains a single-round, manual version of the game where the user can input their choice manually.
Run this file from the terminal to play. No dependencies are required for this file to run.

`python manual_rps.py`

# Camera version of the game

Running the file `camera_rps.py` from the terminal will launch a full game of the camera version of rock-paper-scissors,
where you play against the computer. Follow the instructions on the screen to play. Pressing 'q' between rounds will end
the game early. Before each round, press 'c' to start the countdown timer - display your gesture to the webcam and it will
be captured when the timer reaches zero. Check the terminal for the round result and the current score - first to three rounds
wins the game overall!

`python camera_rps.py`

# The machine learning model

The user gesture is captured by making a prediction of the webcam image content using a [Keras](https://keras.io/about/) machine learning model generated using the web app [Teachable Machine](https://teachablemachine.withgoogle.com).

Chances are, the model contained in
this repository (trained with my gestures, face and background) will not be very good at predicting another user's gestures. Therefore, I'd suggest training your own model.

To do this, visit [Teachable Machine](https://teachablemachine.withgoogle.com) and click on the 'Get Started' button.
