# Computer Vision RPS

This project recreates the classic game Rock-Paper-Scissors, pitting the user against the computer in a best-of-three encounter.
The rules of the game are simple - after a countdown both players present a hand gesture representing one of either Rock, Paper
or Scissors:

![](https://hips.hearstapps.com/hmg-prod/images/people-playing-paper-rock-scissors-royalty-free-illustration-1583269312.jpg?crop=0.994xw:0.799xh;0.00160xw,0.195xh&resize=2048:*)

Rock defeats Scissors, Paper defeats Rock, Scissors defeats Paper. When both players present
the same gesture, the round is a tie.

In a modern twist, the user presents their hand gesture to their computer webcam, the image is captured, computer vision machine 
learning takes over and makes a prediction of which gesture the user presented.