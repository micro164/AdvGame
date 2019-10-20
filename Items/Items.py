from Items.ItemList import Items
from Classes.Classes import Player
from Classes.Classes import Item
from Player.Inventory import inventory_check


def item_list(item_type):
    """Gives a list of items that can be dropped from the monster

    Arguments:
    item_type -- Gives the type (item/weapon/armor) that will be dropped

    """

    temp = {}
    for key, value in list(Items.items()):
        if value[Item.Type] == item_type:
            if (Player.lvl + 5) >= value[Item.lvl] > 0:
                temp[key] = Items[key]
    return temp


def use_item():
    """Allows the user to use an item"""

    print("Enter the name of the item to use")
    input_string = input()
    split = str.split(input_string)
    item_name = split[0]
    amount = split[1] if len(split) == 2 else 1

    check_item = inventory_check(item_name)
    if bool(check_item):
        _check_type(item_name, amount)


def _check_type(item_name, amount):
    for key, value in list(Player.Inventory.items()):
        if key == item_name and value[Item.Type] == "item":
            _adjust_stats(value, item_name, amount)
        elif key == item_name and value[Item.Type] != "item":
            print("\nThis is not an item\n")


def _adjust_stats(value, item_name, amount):
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

    _change_item_count(value, item_name, amount)


def _change_item_count(value, item_name, amount):
    if value[Item.count] > 1:
        value[Item.count] -= amount
    elif value[Item.count] == 1:
        value[Item.count] -= 1
        del Player.Inventory[item_name]
    else:
        print("ERROR: could not use item")


def item_stats():
    """Allows the user to see an items stats"""

    item_lookup = ""

    while item_lookup != "exit":
        print("What item do you want to look up?")
        print("Type exit when done")
        item_lookup = input()

        if item_check(item_lookup) == True and item_lookup != "exit":
            print("Name: " + item_lookup)
            print("Attack: " + str(Items[item_lookup][Item.attack]))
            print("Defense: " + str(Items[item_lookup][Item.defense]))
            print("HP: " + str(Items[item_lookup][Item.HP]))
            print("Price: " + str(Items[item_lookup][Item.price]))
            print("Type: " + Items[item_lookup][Item.Type])
            print("Class: " + Items[item_lookup][Item.Pclass] + "\n")
        elif item_check(item_lookup) == False and item_lookup != "exit":
            print("Item not found\n")


def item_check(item_name):
    """Checks to see if the name entered is actually in the inventory

    Arguments:
    item_name -- name of item that will be checked

    """

    for key, value in list(Items.items()):
        if key == item_name:
            return True
    return False
