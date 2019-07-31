from InventoryAndItems import InvenCheck
from InventoryAndItems import ItemCheck
from InventoryAndItems import Items
from InventoryAndItems import InvenInsert
from Checks import EquipCheck
from Classes import Item
from Classes import Player
import copy

#Delete Equipment item
def DeleteEquip(Etype):
    '''Unequips equipment

    Arguments:
    Etype -- gives the type of the item (weapon/armor/healer/item)

    '''

    temp = EquipTypeCheck(Etype)
    if temp == True:
        item_name = ""
        for key, value in list(Player.Equipment.items()):
            if value[Item.Type] == Etype:
                item_name = key

        if Player.Equipment[item_name][Item.Type] == Etype and Player.Equipment[item_name][Item.count] > 0:
            Player.Strength -= Player.Equipment[item_name][Item.attack]
            Player.Defense -= Player.Equipment[item_name][Item.defense]
            Player.MaxHP -= Player.Equipment[item_name][Item.HP]
            # print("Before Insert: " + str(Player.Inventory[item_name]))
            InvenInsert(item_name)
            # print("After Insert: " + str(Player.Inventory[item_name]))
            del Player.Equipment[item_name]
    else:
        print("ERROR: could not find item in equipment")

#Removing Equipment
def RemoveEquip(item_name):
    '''Checks to see what equipment to remove

    Arguments:
    item_name -- name of the item that is trying to be removed

    '''

    if bool(Player.Equipment) != False:
        temp = ItemCheck(item_name)
        if temp == True:
            if Player.Pclass == Items[item_name][Item.Pclass]:
                if Items[item_name][Item.Type] == 'weapon' and EquipTypeCheck('weapon') == True:
                    DeleteEquip('weapon')
                elif Items[item_name][Item.Type] == 'armor' and EquipTypeCheck('armor') == True:
                    DeleteEquip('armor')
                else:
                    return
            elif Items[item_name][Item.Pclass] == 'healer':
                print("\nERROR: can't equip healing item\n")
            else:
                print("ERROR: can't remove equipment")

        elif temp == False:
            print("This is not an item")
        else:
            print("ERROR: could not find item")

#Inserting Item into equipment
def EquipInsert(item_name):
    '''Equips a weapon or armor to the player

    Arguments:
    item_name -- the name of the weapon or armor being equiped

    '''

    ItemExists = ItemCheck(item_name)
    Equiped = EquipCheck(item_name)

    if ItemExists == True and Equiped == False:
        if Items[item_name][Item.lvl] <= Player.lvl:
            RemoveEquip(item_name)

            if Player.Pclass == Items[item_name][Item.Pclass]:
                kvPair = copy.deepcopy({item_name : Items[item_name]})
                Player.Equipment[item_name] = {}
                Player.Equipment.update(kvPair)
                Player.Strength += Player.Equipment[item_name][Item.attack]
                Player.Defense += Player.Equipment[item_name][Item.defense]
                Player.MaxHP += Player.Equipment[item_name][Item.HP]
                Player.Equipment[item_name][Item.count] += 1

        elif Items[item_name][Item.lvl] > Player.lvl:
            print("\nThis item can not be equiped at this level\n")
        else:
            print("ERROR: Can't equip weapon")
    elif ItemExists == False:
        print("That is not an item")
    elif Equiped == True:
        print("\nYou already have this item equiped\n")
    else:
        print("ERROR: Can't find item")

#Asks the player which item in the inventory they want to equip and equips it
def EquipEquipment():
    '''Menu for the player in order to equip armor and weapons'''

    print("Enter the name of the weapon/armor")
    Equip = input()
    CheckItem = InvenCheck(Equip)
    if bool(CheckItem) == True:
        EquipInsert(Equip)
    else:
        print("ERROR: can not equip item from inventory")

#Checks to see the type of the equipment
def EquipTypeCheck(Etype):
    '''Checks the type of the equipment

    Arguments:
    Etype -- gives the type of the item (weapon/armor/healer/item)

    '''

    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == Etype:
            return True
    return False

#Prints what the player has equiped
def PrintEquip():
    '''Prints the players equipment'''

    for key in Player.Equipment:
        print(key)
