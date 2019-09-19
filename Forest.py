from Classes import Player
from Classes import Directions
from Classes import Features
from Classes import QuestInfo
from Battle import fight
from Checks import CheckHealing
from InventoryAndItems import InvenInsert
from InventoryAndItems import ItemList
from Quests import Quests
from Death import Death
import random

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
            randomPlace = randomSpot(choice)
            DirectionsWent(choice)

            if randomPlace == False:
                Quests()

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

    ## QUESTION: Why do I have choiceList and LastDirections
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

def randomSpot(choice):
    '''Determines if player gets random item, gold, or healing based on directions

    Arguments:
    choice -- The direction the player chooses

    '''

    if len(Features.LastDirections) == 5:
        randDir = []

        for i in range(0, 5):
            randDir.append(str(random.randrange(1, 5)))

        if Features.LastDirections == randDir:
            rand = random.randrange(0,3)

            if rand == 0:
                print("You found an item")
                itemGained = random.choice(list(ItemList('weapon')))
                InvenInsert(itemGained)
                print("A " + itemGained + " was added to your inventory.\n")
            elif rand == 1:
                print("You found some gold")
                randNum = 0
                for char in Player.name:
                    randNum += ord(char)
                goldGained = (Player.lvl * random.randrange(0, randNum)) + Player.lvl
                Player.gold += goldGained
                print(str(goldGained) + " gold was gained.\n")
            elif rand == 2:
                print("You found a fountain of life")
                if Player.hp != Player.MaxHP:
                    perc = random.randint(1, 11)/100
                    Player.hp += Player.MaxHP * perc
                    if Player.hp > Player.MaxHP:
                        Player.hp = Player.MaxHP

                    Player.hp = int(Player.hp)

                    print("Your hp is now: " + str(Player.hp) + "/" + str(Player.MaxHP) + '\n')

                else:
                    print("You don't need more life.\n")

            return True
    return False
