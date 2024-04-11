# AB Challenge 5.2 
# Write a Character Creator program for a role-playing game. The player should be given a pool of 30 points
# to spend on four attributes: Strenght, Health, Wisdom, and Dexterity. The player should be able to spend points on any
# attribute and should also be able to take points from an attribute and put them back into the pool.


def character_creator():
    points = 30
    strength = 0
    health = 0
    wisdom = 0
    dex = 0
    looping = True

    while looping:
        
        print("Your current Attributes are:\n")
        print("Strength  = ", strength)
        print("Health    = ", health)
        print("Wisdom    = ", wisdom)
        print("Dexterity = ", dex)
        print("\nYou have", str(points), "points to use.")
        print(
            """
                WHAT WOULD YOU LIKE TO DO?
                
                0 - Exit
                1 - Increase an Attribute
                2 - Decrease an Attribute
                
                """
            )
        menu = input("Choice: ")
        if menu == "0":
            print("Thanks for playing!")
            input("Press the Enter Key to continue.")
            looping = False
        elif menu == "1":
            if points == 0:
                print("Sorry, you don't have any points left to use. Please remove points from an attribute.")
                input("Press the Enter key to continue.")
            else:
                print("Which Attribute would you like to increase?")
                print(
            """
                0 - Cancel
                1 - Strength
                2 - Health
                3 - Wisdom
                4 - Dexterity
                """
                    )
                attr = input("Choice: ")
                if attr == "1":
                    strength += 1
                    points -= 1
                elif attr == "2":
                    health += 1
                    points -= 1
                elif attr == "3":
                    wisdom += 1
                    points -= 1
                elif attr == "4":
                    dex += 1
                    points -= 1
                elif attr == "0":
                    points = points
        elif menu == "2":
            if points == 30:
                print("Sorry, no attributes currently have points to decrease.")
                input("Press the Enter key to continue.")
            else:
                print("Which Attribute would you like to decrease?")
                print(
                """
                    0 - Cancel
                    1 - Strength
                    2 - Health
                    3 - Wisdom
                    4 - Dexterity
                    """
                    )
                attr = input("Choice: ")
                if attr == "1":
                    if strength > 0:
                        strength -= 1
                        points += 1
                    else:
                        print("There are no points to remove from Strength.")
                        input("Press the Enter key to continue.")
                elif attr == "2":
                    if health > 0:
                        health -= 1
                        points += 1
                    else:
                        print("There are no points to remove from Health.")
                        input("Press the Enter key to continue.")
                elif attr == "3":
                    if wisdom > 0:
                        wisdom -= 1
                        points += 1
                    else:
                        print("There are no points to remove from Wisdom.")
                        input("Press the Enter key to continue.")
                elif attr == "4":
                    if dex > 0:
                        dex -= 1
                        points += 1
                    else:
                        print("There are no points to remove from Dexterity.")
                        input("Press the Enter key to continue.")
                elif attr == "0":
                    points = points

        #looping = False



if __name__ == "__main__":
    character_creator()
