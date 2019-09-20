from Classes import Player
from Classes import Item
import re

def EquipCheck(item_name):
    '''Checks if the player already has the item equiped

    Arguments:
    item_name -- Name of item being checked against players equipment

    '''

    for key, value in list(Player.Equipment.items()):
        if key == item_name:
            return True
    return False

def NameCheck(name):
    '''Checks to see if the player has entered a valid Name

    Arguments:
    name -- Name the player enetered

    '''
    
    if bool(re.compile('[A-Z]', re.IGNORECASE).match(name)) == False:
        print("Name must start with a letter")
        Player.name = input()
        NameCheck(Player.name)

def CheckHealing():
    '''Checks to see if the player has a healing item in his inventory'''

    for key, value in list(Player.Inventory.items()):
        if value[Item.Pclass] == 'healer':
            return True
    return False
