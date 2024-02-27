# AB Challenge 3.4
# Write a program that is the opposite of the "Guess My Number" program.
# Let the user pick a number between 1 and 100, and then try to guess that number based on their input.

import random

def guess_your_num():
    print("\tWelcome to the Guess YOUR Number Game")
    print("\nThink of a number between 1 and 100, and I will attempt to guess your number while keeping track of my guesses.")
    print("Use 'Higher' or 'Lower' to guide the program and enter 'Correct' when I guess the your number.")
    print("Type 'Exit' to leave the program.")

    looping = True
    low_num = 1
    high_num = 100
    attempts = 0

    while looping:
        attempts += 1
        guess = random.randint(low_num, high_num)
        response = input("Are you thinking of the number " + str(guess) + "? ")

        if response == "" or response.lower() == "exit":
            result = print("Thanks for playing!")
            break
        elif response.lower() == "correct":
            result = print("Excellent! That only took " + str(attempts) + " tries!")
            looping = False
        elif response.lower() == "higher":
            low_num = guess + 1
        elif response.lower() == "lower":
            high_num = guess - 1
        else:
            print("You should not be here. How did this happen?")
    return result

if __name__ == "__main__":
    guess_your_num()