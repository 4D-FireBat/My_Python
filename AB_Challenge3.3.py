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
    guess = input("Take a guess: ")
    # print(the_number)
    tries = 10
    # exited = 0
    # ending = ""
    if guess != the_number:
        # tries -= 1
        while guess != the_number:
            # print(guess + " " + str(the_number))
            if guess == "" or guess.lower == "exit":
                result = print("Thanks for playing!")
                break
            else:
                try:
                    tries -= 1
                    if tries == 0:
                        result = print("You have zero tries remaining you fool! How could you possibly NOT know that the number was ", the_number)
                        break
                    guessint = int(guess)
                    if guessint > the_number:
                        print("Lower...")
                        print("You have " + str(tries) + " tries remaining.")
                        #tries -= 1
                    elif guessint < the_number:
                        print("Higher...")
                        print("You have " + str(tries) + " tries remaining.")
                        #tries -= 1
                    elif guessint == the_number:
                        result = print("That's it! I was thinking of the number ", the_number)
                        break
                    guess = input("Guess again: ")
                except ValueError as e:
                    print("Please enter a valid number")
                    print(e)
        return result
    else:
        result = print("That's it! I was thinking of the number ", the_number)
        return result

if __name__ == "__main__":
    you_guess()
