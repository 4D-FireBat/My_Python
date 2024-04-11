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
        looping = False



if __name__ == "__main__":
    character_creator()
