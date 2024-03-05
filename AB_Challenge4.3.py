# AB Challenge 4.3 
# Create a "Word Jumble" game where a list of words are each jumbled and presented to the player to decypher
# Each word presented should be accompanied by a hint that the player can ask for.
# Add a scoring system that rewards the player for solving the word jumble without asking for the hint

import random

def word_jumble():
    # Set a constant list of words to use
    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
    # Pick a word from the list at random and set it to the variable of correct to be checked against later
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    # Scoring system: Guess the word on the first try = 5 points. Guess after the first try, without a hint = 3 points. Using the hint results in only 1 point.
    score = 5

    while word:
        # While there are still letters in the word, use slicing to remove the letters at random and add them to the jumble variable
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    # Start the game
    print(
    """
                    Welcome to Word Jumble!
                    
            Unscramble the letters to make a word
        (Press the Enter key at the prompt to quit.)
        (Enter ? for a hint)
    """
    )
    print("The jumble is:", jumble)
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        if guess == "?":
            print("The first letter of this word is", correct[0])
            guess = input("Your guess: ")
            score = 1
        elif score == 1:
            print("That's incorrect. Guess again.")
            guess = input("Your guess: ")
        else:
            score = 3
            print("That's incorrect. Guess again.")
            guess = input("Your guess: ")
        
    if guess == correct:
        print("That's it! You guessed it! You receive " + str(score) + " points!\n")
        print("Thanks for playing!")
        input("\n\nPress the Enter key to exit")

    


if __name__ == "__main__":
    word_jumble()
