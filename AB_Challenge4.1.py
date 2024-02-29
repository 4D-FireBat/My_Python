# AB Challenge 4.1 
# Write a program that counts for the user. Let the user enter the starting number, 
# the ending number, and the amount to count by.

def counter():
    print("\tWelcomt to The Counter!")
    print("\nThis program will count for you.")

    intstart = int(input("Where would like you for me to start counting? "))
    intend = int(input("What number would you like for me to count to? "))
    denom = int(input("And what number should I count by? "))

    for n in range(intstart,intend + 1,denom):
        print(n)

if __name__ == "__main__":
    counter()