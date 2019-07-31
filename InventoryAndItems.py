from Classes import Item
from Classes import Player
from Checks import EquipCheck
import copy

#Stats for each item in the game
# 0-attack, 1-defense, 2-price, 3-type, 4-Pclass, 5-HP, 6-count, 7-lvl
Items = {'sword': list((10,0,10,'weapon', 'swordsman', 0,0,1)),
         'bronze sword': list((15,0,15,'weapon','swordsman',0,0,5)),
         'iron sword': list((20,0,20,'weapon','swordsman',0,0,10)),
         'steel sword': list((25,0,25,'weapon','swordsman',0,0,15)),
         'long sword': list((30,0,30,'weapon','swordsman',0,0,20)),
         'broad sword': list((40,0,50,'weapon','swordsman',0,0,25)),
         'damascus sword': list((55,0,100,'weapon','swordsman',0,0,30)),
         'Enchanted long sword': list((70,0,150,'weapon','swordsman',0,0,35)),
         'diamond sword': list((100,0,250,'weapon','swordsman',0,0,40)),
         'great sword': list((120,0,300,'weapon','swordsman',0,0,45)),
         'Death sword': list((180,0,400,'weapon','swordsman',0,0,50)),
         'fire sword': list((250,0,600,'weapon','swordsman',0,0,55)),
         'ice sword': list((275,0,650,'weapon','swordsman',0,0,60)),
         'Elemental sword': list((340,0,800,'weapon','swordsman',0,0,65)),
         'sword of ifrit': list((375,0,1000,'weapon','swordsman',0,0,70)),
         'RA\'s sword': list((400,0,1500,'weapon','swordsman',0,0,75)),
         'sword of swords': list((425,0,1800,'weapon','swordsman',0,0,80)),
         'Excalibur': list((475,0,2500,'weapon','swordsman',0,0,85)),
         'elder sword': list((500,0,3000,'weapon','swordsman',0,0,90)),
         'Enchanted ancient sword': list((550,0,4000,'weapon','swordsman',0,0,95)),
         'Dragon sword': list((600,0,5000,'weapon','swordsman',0,0,100)),
         'wand': list((5,0,2,'weapon','wizard',0,0,1)),
         'mace': list((7,0,5,'weapon','wizard',0,0,5)),
         'staff': list((10,0,8,'weapon','wizard',0,0,10)),
         'dagger': list((7,0,5,'weapon','rouge',0,0,1)),
         'bronze dagger': list((10,0,9,'weapon','rouge',0,0,5)),
         'iron dagger': list((15,0,11,'weapon','rouge',0,0,10)),
         'bronze armor': list((0,10,10,'armor','swordsman',0,0,1)),
         'iron armor': list((0,15,15,'armor','swordsman',0,0,5)),
         'steel armor': list((0,25,20,'armor','swordsman',0,0,10)),
         'gold armor': list((0,45,35,'armor','swordsman',10,0,15)),
         'damascus armor': list((0,60,55,'armor','swordsman',0,0,20)),
         'cloth armor': list((0,5,2,'armor','wizard',5,0,1)),
         'hard cloth armor': list((0,7,5,'armor','rouge',0,0,1)),
         'potion': list((0,0,20,'item','healer', 20,0,1)),
         'Hyper Potion': list((0,0,50,'item','healer',50,0,20))}

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
    item_name = input()
    CheckItem = InvenCheck(item_name)
    if bool(CheckItem) == True:
        for key, value in list(Player.Inventory.items()):
            if key == item_name and value[Item.Type] == "item":
                Player.Strength += value[Item.attack]
                print("\n+" + str(value[Item.attack]) + " attack")
                Player.Defense += value[Item.defense]
                print("+" + str(value[Item.defense]) + " defense")
                if Player.hp < Player.MaxHP:
                    Player.hp += value[Item.HP]
                    print("+" + str(value[Item.HP]) + " HP\n")
                if Player.hp > Player.MaxHP:
                    Player.hp = Player.MaxHP

                print("Strength: " + str(Player.Strength))
                print("Defense: " + str(Player.Defense))
                print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp) + "\n")

                if value[Item.count] > 1:
                    value[Item.count] -= 1
                elif value[Item.count] == 1:
                    value[Item.count] -= 1
                    del Player.Inventory[item_name]
                else:
                    print("ERROR: could not use item")
            elif key == item_name and value[Item.Type] != "item":
                print("\nThis is not an item\n")

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
        print(key + " X " + str(value[Item.count]))

def InvenCheck(item_name):
    '''Checks to see if an item is in the players inventory

    Arguments:
    item_name -- name of item being inserted into players inventory

    '''

    for key, value in list(Player.Inventory.items()):
        if key == item_name:
            return True
    return False

def ItemCheck(item_name):
    '''Checks to see if the name entered is actually in the inventory

    Arguments:
    item_name -- name of item that will be chacked

    '''

    for key, value in list(Items.items()):
        if key == item_name:
            return True
    return False
