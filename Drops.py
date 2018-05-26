import random
from InventoryAndItems import ItemList
from Death import Death
from Classes import Player
from InventoryAndItems import InvenInsert

#Determines what type of item will be droped
def MonsterDrop(Mlvl):
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
    random.seed()
    temp = ItemList(Stype)
    key = random.choice(list(temp.items()))
    InvenInsert(key[0])
    print("The monster droped a " + key[0] + ". It has been put in your inventory.\n")
