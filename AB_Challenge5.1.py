# AB Challenge 5.1
# Create a program that prints a list of words in random order.
# The program should print all the words and not repeat any.

import random

def random_words():
    words = ["Khakis", "Dress Shirt", "Jacket", "Exit", "Show", "Scores", "Add", "Delete", "Sort", "Choice"]
    random.shuffle(words)
    for word in words:
        print(word)

    return input("\n\nPress the Enter key to exit.")



if __name__ == "__main__":
    random_words()