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

        print("\tWho's Your Daddy?")
        print("""
        1. Look up a Father
        2. Add a new Father/Son Combo
        3. Exit """)

        option = input("\nWhat would you like to do? ")
        
        if option == "1":
            son = input("\nWho's father are you looking for? ")
            soncap = son.title()
            if soncap in fathers:
                print("I have the father of ", soncap, " listed as: ", fathers.get(soncap))
            else:
                print("I don't have a father listed for ", soncap)
                print("\nWould you like to add them?")
                add = input("Yes or No? ")
                if add.title() == "Yes":
                    newson = soncap.title()
                    dad = input("Who is the father of " + str(newson) + "? ")
                    newfather = dad.title()
                    fathers[newson] = newfather
                    print("\nI now have the father of ", newson, " listed as ", newfather, ".")
                    input("Press the Enter key to continue.")
        
        if option == "2":
            son = input("\nWho is the son that you would like to add? ")
            newson = son.title()
            if newson in fathers:
                print("I currently have ", newson, "'s father listed as", fathers.get(newson))
                print("Would you like to change this record?")
                update = input("Yes or No?")
                if update.title() == "Yes":
                    truefather = input("Who is the true father of " + str(newson) + "? ")
                    newfather = truefather.title()
                    fathers.update(newson = newfather)
                    print("I have updated my records to show that ", fathers.get(newson), " is the father of ", newson, ".")
                    input("\nPress the Enter key to continue.")
            else:
                dad = input("And who would you like to enter as the father of " + newson + " ? ")
                newfather = dad.title()
                fathers[newson] = newfather
                print("\nI now have the father of ", newson, " listed as ", newfather, ".")
                input("Press the Enter key to continue.")


        if option == "3":
            input("Thanks for Playing!")
            run = False




if __name__ == "__main__":
    daddy()
