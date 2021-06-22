from Items.Items import Items
from Items.Items import item_check
from Player.Inventory import print_inventory
from Player.Inventory import inventory_insert
from Player.Equipment import equip_insert
from Utilities.Checks import equip_check
from Classes.Classes import Item
from Classes.Classes import Player
from math import ceil
from Utilities.HelperUtilities import print_slow
from Augment.Augment import augment


def store():
    """Gives the options for the store"""

    print("1.Buy \n2.Sell \n3.Augmentation \n4.Exit")
    choice = input()
    if choice == "1":
        menu_buy()
    elif choice == "2":
        menu_sell()
    elif choice == "3":
        augmentation()
    elif choice == "4":
        print("Thanks for shopping")
    else:
        print("Wrong choice")


def menu_buy():
    """Gives the menu to the player for buying items/weapons/armor"""

    buy = ""

    while buy != '4':
        print("\n1.Weapon \n2.Armor \n3.Item \n4.Exit")
        buy = input()
        if buy == '1':
            sub_menu_buy('weapon')
        elif buy == '2':
            sub_menu_buy('armor')
        elif buy == '3':
            sub_menu_buy('item')
        elif buy == '4':
            print("\nThank you for shopping with us")
            break
        else:
            print("\nERROR: could not buy item\n")


def menu_sell():
    """Menu for player selling an item/armor/weapon"""

    sell = ""
    while sell != "exit":
        print_inventory()
        print_slow("\nWhat item do you want to sell from your inventory?", 0.05)
        print("Type exit to go back")
        sell = input()

        for key, value in list(Player.Inventory.items()):
            if key == sell:
                _sell_item(sell, key, value)


def _sell_item(item_to_sell, key, value):
    gold_gained = ceil((value[Item.price] * .8))
    if value[Item.count] > 1:
        Player.gold += gold_gained
        value[Item.count] -= 1
        print(value[Item.count])
        print("\nYou gained " + str(gold_gained) + " gold.\n")
    elif value[Item.count] == 1:
        if not equip_check(key):
            Player.gold += gold_gained
            value[Item.count] -= 1
            print("\nYou gained " + str(gold_gained) + " gold.\n")
            del Player.Inventory[item_to_sell]
        else:
            print("\nThat item is currently equipped\n")
    else:
        print("\nERROR: Can't sell item\n")


def sub_menu_buy(Stype):
    """Gives the menu for player to buy a weapon, armor, or item

    Arguments:
    Stype -- the type of the item that the player is trying to buy

    """

    print_store(Stype)
    print("Type the name of the " + Stype + " you want to buy or no to exit")
    item_name = input()

    if item_name == 'no':
        print("\nThank you for shopping with us\n")
    elif item_name != 'no':
        if item_check(item_name):
            _check_gold(item_name)
        else:
            print("\nERROR: can't buy item\n")


def _check_gold(item_name):
    price = Items[item_name][Item.price]
    if Player.gold >= price:
        Player.gold -= price
        _check_item_type(item_name)
    else:
        print("\nYou do not have enough money\n")


def _check_item_type(item_name):
    item_type = Items[item_name][Item.Type]
    if item_type != 'item':
        _decide_equip(item_name)
    elif item_type == 'item':
        print("Item put in your inventory.\n")
        inventory_insert(item_name)
    else:
        print("\nERROR: Something went wrong with buying item\n")


def _decide_equip(item_name):
    print("Do you want to equip the " + item_name + ": yes/no")
    choice = input()
    if choice == 'yes':
        _equip_item(item_name)
    elif choice == 'no':
        inventory_insert(item_name)
    else:
        print("\nERROR: Could not put away or equip " + item_name + "\n")


def _equip_item(item_name):
    equip_insert(item_name)
    if Items[item_name][Item.lvl] > Player.lvl:
        inventory_insert(item_name)
        print("The item has been put in your inventory\n")


def print_store(item_type):
    """Prints all the items in the store for the player

    Arguments:
    Stype -- the type of the item that the player is trying to buy

    """

    for key, value in list(Items.items()):
        if (value[Item.Pclass] == Player.Pclass or value[Item.Type] == 'item') and (value[Item.Type] == item_type):
            if Player.lvl <= value[Item.lvl] <= (Player.lvl + 5):
                print(key + ": " + str(value[Item.price]))


def augmentation():
    """Allows the player to augment their weapon or armor"""

    print_slow("\nWelcome to the augmentation center.", 0.05)
    print_slow("Please select what you want to augment", 0.05)
    print("\n1.Weapon \n2.Armor")

    choice = input()

    if choice == "1":
        augment_item("weapon")
    elif choice == "2":
        augment_item("armor")
    else:
        print("wrong key")


def augment_item(type_of_item):
    """Actual augmentation of weapon or armor

    Arguments:
    typeOfItem -- the type of item that the player is trying to augment

    """

    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == type_of_item:
            price = _calculate_augment_price(value)

            print("\nThe price to augment the " + type_of_item + " will be " + str(price) + ".")
            print("Do you accept the charges? (y/n)")

            accept = input()

            if accept == 'y' or accept == 'Y':
                _check_augment_gold(price, type_of_item, value)
            elif accept == 'n' or accept == 'N':
                print("Thank you for coming\n")
            else:
                print("ERROR: wrong key pressed")


def _calculate_augment_price(value):
    char_to_int = 0

    for char in value[Item.Pclass]:
        char_to_int = char_to_int + ord(char)

    return value[Item.lvl] * int((char_to_int / len(value[Item.Pclass])))


def _check_augment_gold(price, type_of_item, value):
    if Player.gold >= price:
        Player.gold = Player.gold - price
        if type_of_item == 'weapon':
            Player.Strength = augment(Player.Strength, value[Item.attack], value[Item.lvl], "weapon", "attack")
        if type_of_item == 'armor':
            Player.Defense = augment(Player.Defense, value[Item.defense], value[Item.lvl], "armor", "defense")
    else:
        print("Not enough gold.\n")

