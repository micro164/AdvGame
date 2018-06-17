from Classes import Player
import random
from Battle import fight
from Checks import CheckHealing

#Introduction to the forest
def ForestIntro():
    if Player.hp > 0:
        print("Welcome to the forest!")
    elif Player.hp <= 0:
        if Player.gold <= 0 and CheckHealing() == False:
            Death()
        else:
            print("You do not have enough hp to fight.")
    else:
        print("ERROR: Can't Access forest")

#For the player to explore
def forest():
    ForestIntro()
    choice = " "
    random.seed()

    while choice != "5" and Player.hp != 0:
        print("1.up \n2.left \n3.right \n4.down \n5.exit")
        choice = input()
        print("")
        if choice >= "1" and choice <= "4":
            rand = random.randrange(0,2)
            if rand == 0:
                print("A group of trees")
            elif rand == 1:
                print("You encountered a monster")
                fight()
            else:
                print("ERROR")
        elif choice == "5":
            print("Leaving forest")
        else:
            print("Wrong choice")