from Classes import Player
from Classes import Item
import re 


# #Checks if item is in player inventory
# def InvenCheck(item_name):
#     for key, value in list(Player.Inventory.items()):
#         if key == item_name:
#             return True
#     return False

#Checks if item is already equiped to player
def EquipCheck(item_name):
    for key, value in list(Player.Equipment.items()):
        if key == item_name:
            return True
    return False

#Check if name is valid
def NameCheck(name):
    if bool(re.compile('[A-Z]', re.IGNORECASE).match(name)) == False:
        print("Name must start with a letter")
        Player.name = input()
        NameCheck(Player.name)

#Checks if player has a healing item in inventory
def CheckHealing():
    for key, value in list(Player.Inventory.items()):
        if value[Item.Pclass] == 'healer':
            return True
    return False
