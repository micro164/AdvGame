from Classes.Classes import Item
from Classes.Classes import Player
from Utilities.Checks import equip_check
from Items.ItemList import Items
from Utilities.HelperUtilities import PrintSlow
import copy


def inventory_insert(item_name):
    """Inserts an item into the players inventory

    Arguments:
    item_name -- name of the item that is being inserted into the inventory

    """

    if item_name in Player.Inventory and equip_check(item_name):
        Player.Inventory[item_name][Item.count] += 1

    else:
        kv_pair = copy.deepcopy({item_name : Items[item_name]})
        Player.Inventory.update(kv_pair)
        Player.Inventory[item_name][Item.count] += 1


def print_inventory():
    """Prints the players inventory"""

    for key, value in list(Player.Inventory.items()):
        PrintSlow(key + " X " + str(value[Item.count]), 0.05)


def inventory_check(item_name):
    """Checks to see if an item is in the players inventory

    Arguments:
    item_name -- name of item being inserted into players inventory

    """

    for key, value in list(Player.Inventory.items()):
        if key == item_name:
            return True
    return False
