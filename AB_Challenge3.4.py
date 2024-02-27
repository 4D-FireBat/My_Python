# AB Challenge 3.4
# Write a program that is the opposite of the "Guess My Number" program.
# Let the user pick a number between 1 and 100, and then try to guess that number based on their input.

import random

def guess_your_num():
    print("\tWelcome to the Guess YOUR Number Game")
    print("\nThink of a number between 1 and 100, and I will attempt to guess your number while keeping track of my guesses.")
    print("Use 'Higher' or 'Lower' to guide the program and enter 'Correct' when I guess the your number.")
    print("Type 'Exit' to leave the program.")

if __name__ == "__main__":
    guess_your_num()