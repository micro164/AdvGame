from Classes import Directions
from Classes import Features
from Classes import Player
from InventoryAndItems import InvenInsert
from InventoryAndItems import ItemList
import random

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
                _foundItem()
            elif rand == 1:
                _foundGold()
            elif rand == 2:
                _foundLife()

            return True
    return False

def _foundItem():
    print("You found an item")
    itemGained = random.choice(list(ItemList('weapon')))
    InvenInsert(itemGained)
    print("A " + itemGained + " was added to your inventory.\n")

def _foundGold():
    print("You found some gold")
    randNum = 0
    for char in Player.name:
        randNum += ord(char)
    goldGained = (Player.lvl * random.randrange(0, randNum)) + Player.lvl
    Player.gold += goldGained
    print(str(goldGained) + " gold was gained.\n")

def _foundLife():
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
