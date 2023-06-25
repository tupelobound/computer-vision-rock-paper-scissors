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



