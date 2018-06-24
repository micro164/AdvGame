from Classes import Player
from Classes import Directions
from Classes import Features
from Classes import QuestInfo
import random
from Battle import fight
from Checks import CheckHealing
from InventoryAndItems import InvenInsert
from Quests import Quests
from Death import Death

#Introduction to the forest
def ForestIntro():
    '''The introduction to entering the forest'''

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
    '''The menu for exploring the forest'''

    ForestIntro()
    choice = " "
    random.seed()

    while choice != "5" and Player.hp != 0:
        print("1.up \n2.left \n3.right \n4.down \n5.exit")
        choice = input()
        print("")

        if choice >= "1" and choice <= "4":

            DublicateItem(choice)
            DirectionsWent(choice)
            Quests() # TODO: Find a better place for this so after presenting the quest it doesn't go directly to battle

            if QuestInfo.InQuest == False:
                rand = random.randrange(0,2)

                if rand == 0:
                    print("A group of trees")
                elif rand == 1:
                    print("You encountered a monster")
                    fight()
                else:
                    print("ERROR")
            else:
                QuestInfo.InQuest = False
        elif choice == "5":
            print("Leaving forest")
        else:
            print("Wrong choice")

def DublicateItem(choice):
    '''Dubplicates an item in the players Inventory when the correct sequence is pushed

    Arguments:
    choice -- The direction that the player chooses

    '''

    dublicationCheck = [Directions.LEFT.value, Directions.LEFT.value, Directions.UP.value, Directions.RIGHT.value, Directions.DOWN.value]

    Features.choiceList.append(choice)

    if len(Features.choiceList) == 5:
        if Features.choiceList == dublicationCheck:
            InvenInsert(list(Player.Inventory.keys())[random.randrange(0, len(list(Player.Inventory.keys())))])
        Features.choiceList.clear()

def DirectionsWent(choice):
    '''Keeps track of the last 5 directions the player went

    Arguments:
    choice -- The direction the player chooses

    '''

    if len(Features.LastDirections) == 5:
        Features.LastDirections.clear()

    Features.LastDirections.append(choice)
