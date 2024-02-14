# AB Challenge 3.1
# Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random.
# each time it runs.

import random

def forutne_cookie():
    which = random.randint(1,5)
    fortune = ""
    if which == 1:
        fortune = print("Do not be afraid of competition.\n")
    elif which == 2:
        fortune = print("An exciting opportunity lies ahead of you.\n")
    elif which == 3:
        fortune = print("You will always be surrounded by true friends.\n")
    elif which == 4:
        fortune = print("Don't hold onto things. that require a tight grip.\n")
    elif which == 5:
        fortune = print("Little by little one travels far.\n")
    return fortune

if __name__ == "__main__":
    forutne_cookie()
