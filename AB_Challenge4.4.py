# AB Challenge 4.4 
# Create a game where the computer picks a random word and the player has to guess that word.
# The computer tells the player how many letters are in teh word. Then the player gets five chances to ask if a letter is in the word.
# The computer can only respond with "yes" or "no". Then the player must guess the word.

import random

def not_hangman():
    # Set a constant list of words to choose from
    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
    # Pick a word from the list at random and set it to the variable of correct to be checked against later
    word = random.choice(WORDS)
    count = 5

    print(
    """
                    Welcome to NOT Hangman!
                
        I'm thinking of a word. You will be given 5 chances to guess letters in that word.
        I will only tell you if the letters you guess are in the word or not. After 5 letters,
        you mush attempt to guess the word.
    """
    )
    print("Your word is " + str(len(word)) + " letters long.")

    while count > 0:
        count -= 1
        letter = input("Please choose a letter: ")
        if letter in word:
            print("yes")
        else:
            print("no")
    
    print("No more letters. Try guessing the word.")
    guess = input("Your guess: ")

    if guess == word:
        print("That's it! You guessed the right word!")
    else:
        print("Sorry, that's incorrect. Please play again.")

    input("Press the Enter key to exit.")



if __name__ == "__main__":
    not_hangman()
