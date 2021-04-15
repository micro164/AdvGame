from Classes.Classes import *
from Player.Inventory import inventory_insert
from Items.Items import item_list
import random


def duplicate_item(choice):
    """Duplicates an item in the players Inventory when the correct sequence is pushed

    Arguments:
    choice -- The direction that the player chooses

    """

    duplication_check = [Directions.LEFT.value, Directions.LEFT.value, Directions.UP.value, Directions.RIGHT.value, Directions.DOWN.value]

    # QUESTION: Why do I have choiceList and LastDirections
    Features.choiceList.append(choice)

    if len(Features.choiceList) == 5:
        if Features.choiceList == duplication_check:
            inventory_insert(list(Player.Inventory.keys())[random.randrange(0, len(list(Player.Inventory.keys())))])
        Features.choiceList.clear()


def random_spot():
    if len(Features.LastDirections) == 5:
        rand_dir = []

        for i in range(0, 5):
            rand_dir.append(str(random.randrange(1, 5)))

        if Features.LastDirections == rand_dir:
            rand = random.randrange(0, 3)

            if rand == 0:
                _found_item()
            elif rand == 1:
                _found_gold()
            elif rand == 2:
                _found_life()

            return True
    return False


def _found_item():
    print("You found an item")
    item_gained = random.choice(list(item_list('weapon')))
    inventory_insert(item_gained)
    print("A " + item_gained + " was added to your inventory.\n")


def _found_gold():
    print("You found some gold")
    rand_num = 0
    for char in Player.name:
        rand_num += ord(char)
    gold_gained = (Player.lvl * random.randrange(0, rand_num)) + Player.lvl
    Player.gold += gold_gained
    print(str(gold_gained) + " gold was gained.\n")


def _found_life():
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
