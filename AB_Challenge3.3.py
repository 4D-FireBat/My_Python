# AB Challenge 3.3
# Write a 'Guess My Number' program that picks a number at random, and gives the user
# A limited number of guesses and presents an appropriately chastising message if they don't guess correctly.

import random

def you_guess():
    # Game Introduction:
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it within 10 guesses.\n")
    print("You can press the Enter key without a guess to exit the game.\n\n")

    # Set the initial variables
    the_number = random.randint(1, 100)
    #guess = input("Take a guess: ")
    print(the_number)
    tries = 10
    exited = 0
    ending = ""

    # Guessing loop
    looping = True
    while looping:
        guess = input("Take a guess: ")
        if tries == 1:
            exited = 1
            looping = False
        if guess == "":
            exited = 1
            looping = False
        else: 
            guessint = int(guess)
        if guessint > the_number:
            print("Lower...")
            tries -= 1
            print("You have " + str(tries) + " tries left")
        elif guessint < the_number:
            print("Higher...")
            tries -= 1
            print("You have " + str(tries) + " tries left")
        else:
            exited = 0
            guess = the_number
            looping = False
        
    if guess == the_number and exited == 0:
        ending = print("You guessed it! The number was", the_number)
    elif tries == 1 and exited == 1:
        ending = print("You absolute fool! How could you not know I was thinking of the number " +  str(the_number) + "?")
    elif exited == 1:
        ending = print("Thanks for playing!")

    return ending

if __name__ == "__main__":
    you_guess()
