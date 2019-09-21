from Classes.Classes import Item
from Classes.Classes import Player
from Utilities.Checks import EquipCheck
from Items.ItemList import Items
from Utilities.HelperUtilities import PrintSlow
import copy

def InvenInsert(item_name):
    '''Inserts an item into the players inventory

    Arguments:
    item_name -- name of the item that is being inserted into the inventory

    '''

    Echeck = EquipCheck(item_name)
    if item_name in Player.Inventory and Echeck == False:
        Player.Inventory[item_name][Item.count] += 1

    else:
        kvPair = copy.deepcopy({item_name : Items[item_name]})
        Player.Inventory.update(kvPair)
        Player.Inventory[item_name][Item.count] += 1

def PrintInven():
    '''Prints the players inventory'''

    for key, value in list(Player.Inventory.items()):
        PrintSlow(key + " X " + str(value[Item.count]), 0.05)

def InvenCheck(item_name):
    '''Checks to see if an item is in the players inventory

    Arguments:
    item_name -- name of item being inserted into players inventory

    '''

    for key, value in list(Player.Inventory.items()):
        if key == item_name:
            return True
    return False
