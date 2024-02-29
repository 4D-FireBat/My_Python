# AB Challenge 4.2 
# Create a program that takes an input from the user and then prints that same input backwards.

def reverse():
    response = input("Please input a word or phrase: ")
    reverse = response[::-1]

    print(reverse)
    input("\n\nPress the enter key to exit: ")

if __name__ == "__main__":
    reverse()
