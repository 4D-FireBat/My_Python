# AB Challenge 3.2
# Write a program that flips a coin 100 times and then tells you the number of Heads and Tails.

import random

def coin_flipper():
    heads = 0
    tails = 0
    flips = 0
    
    while flips < 100:
        flip = random.randint(1,2)
        if flip == 1:
            heads += 1
            flips += 1
        else:
            tails += 1
            flips += 1
    result = print("After 100 coin flips, the results are " + str(heads) + " heads and " + str(tails) + " tails.")
    return result

if __name__ == "__main__":
    coin_flipper()
