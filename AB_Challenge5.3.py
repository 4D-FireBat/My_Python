# AB Challenge 5.3 
# Write a Who's Your Daddy? program that lets the user enter the name of a male and produces the name of his father.
# (You can use celebrities, fictional characters, or even Historical figures for fun.) Allow the user to add, replace and delete son-father pairs.

def daddy():
    fathers = {"Luke Skywalker":"Anakin Skywalker",
               "Emilio Estevez":"Martin Sheen",
               "Charlie Sheen":"Martin Sheen",
               "Jason Doyle":"Randy Doyle",
               "Justin Doyle":"Randy Doyle",
               "Randy Doyle":"Henry Doyle",
               "Nemo":"Marlin"}
    run = True
    while run:
        son = input("Who's father are you looking for?")
        soncap = son.title()
        if soncap in fathers:
            print("I have the father of ", soncap, " listed as: ", fathers.get(soncap))
        else:
            print("I don't have a father listed for ", soncap)
            print("\nWould you like to add them?")
            add = input("Yes or No?")



if __name__ == "__main__":
    daddy()
