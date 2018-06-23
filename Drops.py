import random

from InventoryAndItems import InvenInsert
from InventoryAndItems import ItemList
from Classes import Player

#Determines what type of item will be droped
def MonsterDrop(Mlvl):
    '''Determines what type of item a monster will drop

    Arguments:
    Mlvl - The level of the monster

    '''

    random.seed()
    chance = random.random()

    if chance > 0.5 and chance < 0.7:
        Drop('item')
    elif chance >= 0.7 and chance < 0.8:
        chance2 = random.random()
        if chance2 < 0.5:
            Drop('armor')
        elif chance2 >= 0.5:
            Drop('weapon')
        else:
            print("ERROR: could not drop weapon/armor")
    elif chance >= 0.8:
        GoldGained = random.randrange(0, Mlvl * 10) + 10
        print("The monster droped " + str(GoldGained) + " gold.\n")
        Player.gold += GoldGained
    elif chance <= 0.5:
        print("The monster did not drop anything.\n")
    else:
        print("ERROR: Could not drop item.")

#Function for randomly droping items when monster dies
def Drop(Stype):
    '''Determines what items drop from the monster

    Arguments:
    Stype -- The type of the item being dropped

    '''

    random.seed()
    temp = ItemList(Stype)
    key = random.choice(list(temp.items()))
    InvenInsert(key[0])
    print("The monster droped a " + key[0] + ". It has been put in your inventory.\n")

def QuestReward():
    '''Determines the reward for completing the quest'''

    random.seed()
    chance = random.random()

    if chance > 0 and chance < 0.5:
        Drop('item')
    elif chance >= 0.5 and chance < 1:
        chance2 = random.random()
        if chance2 < 0.5:
            Drop('armor')
        elif chance2 >= 0.5:
            Drop('weapon')
        else:
            print("ERROR: could not drop weapon/armor")
    else:
        print("ERROR: Could not drop item.")
