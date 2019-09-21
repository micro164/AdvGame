from Items.ItemList import Items
from Classes.Classes import Player
from Classes.Classes import Item
from Player.Inventory import InvenCheck

def ItemList(Stype):
    '''Gives a list of items that can be dropped from the monster

    Arguments:
    Stype -- Gives the type (item/weapon/armor) that will be dropped

    '''

    temp = {}
    for key, value in list(Items.items()):
        if value[Item.Type] == Stype:
            if value[Item.lvl] <= (Player.lvl + 5) and value[Item.lvl] > 0:
                temp[key] = Items[key]
    return temp

def UseItem():
    '''Allows the user to use an item'''

    print("Enter the name of the item to use")
    inputString = input()
    split = str.split(inputString)
    item_name = split[0]
    amount = split[1] if len(split) == 2 else 1

    CheckItem = InvenCheck(item_name)
    if bool(CheckItem) == True:
        _checkType(item_name, amount)

def _checkType(item_name, amount):
    for key, value in list(Player.Inventory.items()):
        if key == item_name and value[Item.Type] == "item":
            _adjustStats(value, item_name, amount)
        elif key == item_name and value[Item.Type] != "item":
            print("\nThis is not an item\n")

def _adjustStats(value, item_name, amount):
    Player.Strength += (value[Item.attack] * int(amount))
    print("\n+" + str(value[Item.attack]) + " attack")

    Player.Defense += (value[Item.defense] * int(amount))
    print("+" + str(value[Item.defense]) + " defense")

    if Player.hp < Player.MaxHP:
        Player.hp += (value[Item.HP] * int(amount))
        print("+" + str(value[Item.HP]) + " HP\n")

    if Player.hp > Player.MaxHP:
        Player.hp = Player.MaxHP

    print("Strength: " + str(Player.Strength))
    print("Defense: " + str(Player.Defense))
    print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp) + "\n")

    _changeItemCount(value, item_name, amount)


def _changeItemCount(value, item_name, amount):
    if value[Item.count] > 1:
        value[Item.count] -= amount
    elif value[Item.count] == 1:
        value[Item.count] -= 1
        del Player.Inventory[item_name]
    else:
        print("ERROR: could not use item")

def ItemStats():
    '''Allows the user to see an items stats'''

    item_lookup = ""

    while item_lookup != "exit":
        print("What item do you want to look up?")
        print("Type exit when done")
        item_lookup = input()

        if ItemCheck(item_lookup) == True and item_lookup != "exit":
            print("Name: " + item_lookup)
            print("Attack: " + str(Items[item_lookup][Item.attack]))
            print("Defense: " + str(Items[item_lookup][Item.defense]))
            print("HP: " + str(Items[item_lookup][Item.HP]))
            print("Price: " + str(Items[item_lookup][Item.price]))
            print("Type: " + Items[item_lookup][Item.Type])
            print("Class: " + Items[item_lookup][Item.Pclass] + "\n")
        elif ItemCheck(item_lookup) == False and item_lookup != "exit":
            print("Item not found\n")

def ItemCheck(item_name):
    '''Checks to see if the name entered is actually in the inventory

    Arguments:
    item_name -- name of item that will be chacked

    '''

    for key, value in list(Items.items()):
        if key == item_name:
            return True
    return False
