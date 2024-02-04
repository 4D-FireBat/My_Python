# LinkedIn Learning Palindrome Challenge
# Create a function that takes a given string and return a Boolean value indicating whether the string is a palindrome or not.

def is_palindrome(teststr):
    # Remove capitalization
    teststr = teststr.lower()
    # Create a new string that removes all punctionation and spaces from the original string
    newstr = ""
    for c in teststr:
        if c.isalnum():
            newstr += c
    # If the new string is the same forwards and backwards then return true
    if newstr == newstr[::-1]:
        return True
    return False


