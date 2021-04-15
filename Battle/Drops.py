import random

from Player.Inventory import inventory_insert
from Items.Items import item_list
from Classes.Classes import Player


def monster_drop(monster_lvl):
    """Determines what type of item a monster will drop

    Arguments:
    monster_lvl - The level of the monster

    """

    random.seed()
    chance = random.random()

    if 0.5 < chance < 0.7:
        drop('item')
    elif 0.7 <= chance < 0.8:
        chance2 = random.random()
        if chance2 < 0.5:
            drop('armor')
        elif chance2 >= 0.5:
            drop('weapon')
        else:
            print("ERROR: could not drop weapon/armor")
    elif chance >= 0.8:
        gold_gained = random.randrange(0, monster_lvl * 10) + 10
        print("The monster dropped " + str(gold_gained) + " gold.\n")
        Player.gold += gold_gained
    elif chance <= 0.5:
        print("The monster did not drop anything.\n")
    else:
        print("ERROR: Could not drop item.")


def drop(item_type):
    """Determines what items drop from the monster

    Arguments:
    item_type -- The type of the item being dropped

    """

    random.seed()
    temp = item_list(item_type)
    key = random.choice(list(temp.items()))
    inventory_insert(key[0])
    print("The monster dropped a " + key[0] + ". It has been put in your inventory.\n")


def quest_drop(item_type):
    """Determines what quest reward will be

    Arguments:
    item_type -- The type of the item being dropped

    """

    random.seed()
    i_list = item_list(item_type)
    item = random.choice(list(i_list.items()))
    inventory_insert(item[0])
    print("You got a " + item[0] + " for you efforts. It has been put in your inventory.\n")


def quest_reward():
    """Determines the reward for completing the quest"""

    random.seed()
    chance = random.random()

    if 0 < chance < 0.5:
        quest_drop('item')
    elif 0.5 <= chance < 1:
        chance2 = random.random()
        if chance2 < 0.5:
            quest_drop('armor')
        elif chance2 >= 0.5:
            quest_drop('weapon')
        else:
            print("ERROR: could not drop weapon/armor")
    else:
        print("ERROR: Could not drop item.")
