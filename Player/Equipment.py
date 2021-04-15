from Player.Inventory import inventory_check
from Items.Items import item_check
from Items.Items import Items
from Player.Inventory import inventory_insert
from Utilities.Checks import equip_check
from Classes.Classes import Item
from Classes.Classes import Player
from Utilities.HelperUtilities import print_text
import copy


def delete_equip(Etype):
    '''Unequips equipment

    Arguments:
    Etype -- gives the type of the item (weapon/armor/healer/item)

    '''

    temp = equip_type_check(Etype)
    if temp:
        item_name = _find_item_name(Etype)

        if Player.Equipment[item_name][Item.Type] == Etype and Player.Equipment[item_name][Item.count] > 0:
            Player.Strength -= Player.Equipment[item_name][Item.attack]
            Player.Defense -= Player.Equipment[item_name][Item.defense]
            Player.MaxHP -= Player.Equipment[item_name][Item.HP]
            inventory_insert(item_name)
            del Player.Equipment[item_name]
    else:
        print("ERROR: could not find item in equipment")


def _find_item_name(Etype):
    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == Etype:
            return key


def remove_equip(item_name):
    '''Checks to see what equipment to remove

    Arguments:
    item_name -- name of the item that is trying to be removed

    '''

    if bool(Player.Equipment):
        temp = item_check(item_name)
        if temp:
            check_item_class(item_name)
        elif not temp:
            print("This is not an item")
        else:
            print("ERROR: could not find item")


def check_item_class(item_name):
    if Player.Pclass == Items[item_name][Item.Pclass]:
        check_equipment_type(item_name)
    elif Items[item_name][Item.Pclass] == 'healer':
        print("\nERROR: can't equip healing item\n")
    else:
        print("ERROR: can't remove equipment")


def check_equipment_type(item_name):
    if Items[item_name][Item.Type] == 'weapon' and equip_type_check('weapon') == True:
        delete_equip('weapon')
    elif Items[item_name][Item.Type] == 'armor' and equip_type_check('armor') == True:
        delete_equip('armor')


def equip_insert(item_name):
    '''Equips a weapon or armor to the player

    Arguments:
    item_name -- the name of the weapon or armor being equiped

    '''

    ItemExists = item_check(item_name)
    Equiped = equip_check(item_name)

    if ItemExists is True and Equiped is False:
        _compare_item_and_player_level(item_name)
    elif not ItemExists:
        print("That is not an item")
    elif Equiped:
        print("\nYou already have this item equiped\n")
    else:
        print("ERROR: Can't find item")


def _compare_item_and_player_level(item_name):
    if Items[item_name][Item.lvl] <= Player.lvl:
        remove_equip(item_name)

        if Player.Pclass == Items[item_name][Item.Pclass]:
            kvPair = copy.deepcopy({item_name: Items[item_name]})
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


def equip_equipment():
    '''Menu for the player in order to equip armor and weapons'''

    print("Enter the name of the weapon/armor")
    equip = input()
    check_item = inventory_check(equip)
    if bool(check_item):
        equip_insert(equip)
    else:
        print("ERROR: can not equip item from inventory")


def equip_type_check(Etype):
    '''Checks the type of the equipment

    Arguments:
    Etype -- gives the type of the item (weapon/armor/healer/item)

    '''

    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == Etype:
            return True
    return False


def print_equip():
    '''Prints the players equipment'''

    for key in Player.Equipment:
        print_text(key)
