#!/usr/bin/python3

#Author: Jonathon Bryant
#Date Created: 9/22/17
#Date Modified: 12/29/17
#This is a simple text based game created in the language of python

#-----------------------IMPORTS-----------------------------

from enum import IntEnum
import random
from math import ceil
from math import floor
import re

#-----------------------ITEMS-------------------------------

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
         'dagger': list((7,0,5,'weapon','rouge',0,0,1)),
         'bronze armor': list((0,10,10,'armor','swordsman',0,0,1)),
         'cloth armor': list((0,5,2,'armor','wizard',5,0,1)),
         'hard cloth armor': list((0,7,5,'armor','rouge',0,0,1)),
         'potion': list((0,0,20,'item', 'healer', 20,0,1))}

#------------------------MONSTERS----------------------------

#Stats for monsters
# 0-HP, 1-attack, 2-defense, 3-exp, 4.lvl, 5.MaxHP
Monsters = {'rat':              list((50,   10,      7,      10,     1,   50)),
            'Wild Chicken':     list((10,   12,      5,      5,      1,   10)),
            'Spider':           list((25,   15,     10,      15,     3,   25)),
            'goblin':           list((100,  17,     7,      50,     5,   100)),
            'Giant Spider':     list((75,   19,     15,     75,     10,  75)),
            'Giant Rat':        list((100,  16,     18,     100,    12,  100)),
            'Armored Goblin':   list((150,  20,     25,     125,    15,  150)),
            'Zombie':           list((250,  30,     10,     150,    17,  250)),
            'Goblin Zombie':    list((400,  45,     10,     200,    20,  400)),
            'Wolf':             list((200,  55,     35,     190,    23,  200)),
            'Undead Wolf':      list((400,  70,     20,     250,    25,  400)),
            'Ghost':            list((500,  50,     25,     225,    30,  500)),
            'Ghoul':            list((425,  60,     40,     300,    35,  425)),
            'Vampire':          list((650,  90,     60,     500,    40,  650)),
            'Cyclops':          list((700,  80,     100,    525,    45,  700)),
            'Mummy':            list((675,  85,     65,     550,    50,  675)),
            'Earth Elemental':  list((800,  70,     120,    700,    55,  800)),
            'Wind Elemental':   list((750,  40,     100,    700,    55,  750)),
            'Fire Elemental':   list((710,  120,    110,    700,    55,  710)),
            'Water Elemental':  list((850,  80,     100,    700,    55,  850)),
            'Basilisk':         list((900,  100,    90,     800,    60,  900)),
            'Angel':            list((1000, 120,    100,    1000,   65,  1000)),
            'Griffon':          list((1125, 150,    125,    1300,   70,  1125)),
            'Baby Dragon':      list((1500, 200,    175,    2000,   75,  1500)),
            'Ifrit':            list((1700, 250,    150,    1800,   80,  1700)),
            'Phoenix':          list((2000, 275,    250,    2400,   85,  2000)),
            'Adamantoise':      list((3000, 100,    500,    2200,   90,  3000)),
            'Elder Lich':       list((3500, 300,    275,    2500,   95,  3500)),
            'Dragon':           list((5000, 800,    750,    5000,   100, 5000))}

#------------------------CLASSES-----------------------------

#Player stats
class Player:
    name = ""
    MaxHP = 0
    hp = 0
    Strength = 0
    Defense = 0
    gold = 0
    MaxExp = 100
    exp = 0
    lvl = 1
    Pclass = ""
    Inventory = dict()
    Equipment = dict()

#Monster Class
class Monster(IntEnum):
    HP = 0
    attack = 1
    defense = 2
    exp = 3
    lvl = 4
    MaxHP = 5

#Item Class
class Item(IntEnum):
    attack = 0
    defense = 1
    price = 2
    Type = 3
    Pclass = 4
    HP = 5
    count = 6
    lvl = 7

#-----------------------FUNCTIONS-----------------------------

#Delete Equipment item
def DeleteEquip(Etype):
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
            InvenInsert(item_name)
            del Player.Equipment[item_name]
    elif temp == False:
        print("Item not in equipment")
    else:
        print("ERROR: could not find item in equipment")

#Removing Equipment
def RemoveEquip(item_name):
    if bool(Player.Equipment) != False:
        temp = ItemCheck(item_name)
        if temp == True:
            if Player.Pclass == Items[item_name][Item.Pclass]:
                if Items[item_name][Item.Type] == 'weapon' and EquipTypeCheck('weapon') == True:
                    DeleteEquip('weapon')
                elif Items[item_name][Item.Type] == 'weapon' and EquipTypeCheck('weapon') == False:
                    return

                if Items[item_name][Item.Type] == 'armor' and EquipTypeCheck('armor') == True:
                    DeleteEquip('armor')
                elif Items[item_name][Item.Type] == 'armor' and EquipTypeCheck('armor') == False:
                    return
            else:
                print("ERROR: can't remove equipment")

        elif temp == False:
            print("This is not an item")
        else:
            print("ERROR: could not find item")

#Inserting Item into equipment
def EquipInsert(item_name):
    temp = ItemCheck(item_name)

    if temp == True:
        if Items[item_name][Item.lvl] <= Player.lvl:
            RemoveEquip(item_name)

            if Player.Pclass == Items[item_name][Item.Pclass]:
                Player.Equipment[item_name] = Items[item_name]
                Player.Strength += Player.Equipment[item_name][Item.attack]
                Player.Defense += Player.Equipment[item_name][Item.defense]
                Player.MaxHP += Player.Equipment[item_name][Item.HP]
                Player.Equipment[item_name][Item.count] += 1

        elif Items[item_name][Item.lvl] > Player.lvl:
            print("This item can not be equiped at this level")
        else:
            print("ERROR: Can't equip weapon")
    elif temp == False:
        print("That is not an item")
    else:
        print("ERROR: Can't find item")

#Inserting Item into inventory
def InvenInsert(item_name):
    Player.Inventory[item_name] = Items[item_name]
    Echeck = EquipCheck(item_name)
    if Echeck == False:
        Player.Inventory[item_name][Item.count] += 1

#Check if name is valid
def NameCheck(name):
    if bool(re.compile('[A-Z]', re.IGNORECASE).match(name)) == False:
        print("Name must start with a letter")
        Player.name = input()
        NameCheck(Player.name)

#Game Intro
def GameIntro():
    print("Welcome to TxtBasedAdv")
    print("Please enter a name: ")
    Player.name = input()
    NameCheck(Player.name)
    print("Hello " + Player.name)

    print("\nChoose your class")
    print("1.Swordsman Class \n2.Wizard Class \n3.Rogue Class")
    choice = input()

    #Choosing a class
    if choice == "1":
        print("Welcome to the swordsman class\n")
        Player.Pclass = 'swordsman'
        Player.Strength = 10
        Player.Defense = 10
        Player.hp = 100
        Player.MaxHP = 100
        EquipInsert('sword')
        print("You have been given a sword.")
        EquipInsert('bronze armor')
        print("You have been given a bronze armor\n")
        Intro()
    elif choice == "2":
        print("Welcome to the wizard class\n")
        Player.Pclass = 'wizard'
        Player.Strength = 5
        Player.Defense = 3
        Player.hp = 50
        Player.MaxHP = 50
        EquipInsert('wand')
        print("You have been given a wand.")
        EquipInsert('cloth armor')
        print("You have been given a cloth armor\n")
        Intro()
    elif choice == "3":
        print("Welcome to the rogue class\n")
        Player.Pclass = 'rouge'
        Player.Strength = 7
        Player.Defense = 5
        Player.hp = 70
        Player.MaxHP = 70
        EquipInsert('dagger')
        print("You have been given a dagger.")
        EquipInsert('hard cloth armor')
        print("You have been given a hard cloth armor.\n")
        Intro()
    else:
        print("Wrong choice")
        GameIntro()

#Gives the player a potion to survive and an awsome introduction to the game
def Intro():
    InvenInsert('potion')

    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")

#List of monsters that appear in the forest
def MonsterList():
    temp = {}
    for key, value in list(Monsters.items()):
        if value[Monster.lvl] >= Player.lvl and value[Monster.lvl] <= (Player.lvl + 5):
            temp[key] = Monsters[key]
    return temp

#Player encounters a random monster
def fight():
    temp = MonsterList()
    random.seed()
    key = random.choice(list(temp.items()))
    value = key[1]
    print("It's a " + key[0])
    Pdamage = 0
    Edamage = 0

    while Player.hp > 0 and value[Monster.HP] > 0:
        Pdamage = random.randrange(Player.Strength) - (random.randrange(value[Monster.defense]) + value[Monster.lvl])
        Edamage = (random.randrange(value[Monster.attack]) + value[Monster.lvl]) - (random.randrange(Player.Defense) + (Player.lvl * 2)) 

        if Pdamage < 0:
            Pdamage = 0

        if Edamage < 0:
            Edamage = 0
    

        print("You hit the " + key[0] + " for " + str(Pdamage) + " damage")
        value[Monster.HP] -= Pdamage
        print(key[0] + " now has " + str(value[Monster.HP]) + " life left.")
        if value[Monster.HP] <= 0:
            break
        print(key[0] + " hit you for " + str(Edamage) + " damage")
        Player.hp -= Edamage
        print("You have " + str(Player.hp) + " life left.")

    print("")

    if value[Monster.HP] < value[Monster.MaxHP]:
        value[Monster.HP] = value[Monster.MaxHP]

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")

    if Player.hp > 0:
        print("YOU WON!!!")
        exp = random.randrange(0, value[Monster.exp]) + value[Monster.lvl]
        Player.exp += exp
        print("You gained " + str(exp) + " exp")
        LevelUp()
        print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
        MonsterDrop(value[Monster.lvl])

    Death()

#Revives player when there is no way to gain hp
def Death():
    if Player.hp == 0 and Player.gold == 0:
        HealingItem = CheckHealing()
        if bool(HealingItem) == False and Player.exp > 0:
            print("Grim Reaper: 'You have no gold to heal yourself. Muhahaha'")
            print("Grim Reaper: 'I will take some experience from you in order to restore your life.'")
            print("")
            Player.exp -= 10 * Player.lvl
            if Player.exp < 0:
                Player.exp = 0
            Player.hp = Player.MaxHP
        elif Player.exp == 0 and bool(HealingItem) == False:
            print("Grim Reaper: 'You have nothing so I will add to your Max Exp. to restore your life.'")
            print("")
            Player.MaxExp += 10 * Player.lvl
            Player.hp = Player.MaxHP

#Checks if player has a healing item in inventory
def CheckHealing():
    for key, value in list(Player.Inventory.items()):
        if value[Item.Pclass] == 'healer':
            return True
    return False

#List of items that monsters drop
def ItemList(Stype):
    temp = {}
    for key, value in list(Items.items()):
        if value[Item.Type] == Stype:
            if value[Item.lvl] <= (Player.lvl + 5):
                temp[key] = Items[key]
    return temp

#Function for randomly droping items when monster dies
def Drop(Stype):
    random.seed()
    temp = ItemList(Stype)
    key = random.choice(list(temp.items()))
    InvenInsert(key[0])
    print("The monster droped a " + key[0] + ". It has been put in your inventory.\n")

#Determines what type of item will be droped
def MonsterDrop(Mlvl):
    random.seed()
    chance = random.random()

    if chance > 0.5 and chance < 0.7:
        Drop('item')
    elif chance >= 0.7 and chance < 0.8:
        chance2 = random.random()
        if chance2 < 0.5:
            Drop('armor')
        elif chance2 >= 0.5:
            Drop('weapon')
        else:
            print("ERROR: could not drop weapon/armor")
    elif chance >= 0.8:
        GoldGained = random.randrange(0, Mlvl * 10) + 10
        print("The monster droped " + str(GoldGained) + " gold.\n")
        Player.gold += GoldGained
    elif chance <= 0.5:
        print("The monster did not drop anything.\n")
    else:
        print("ERROR: Could not drop item.")

#Function for checking if the player can level up and to adjust the stats of the player
def LevelUp():
    while Player.exp >= Player.MaxExp and Player.lvl < 100:
        print("YOU LEVELED UP!!!!!")
        Player.lvl += 1
        print("You are now level " + str(Player.lvl))
        Player.MaxExp += floor((Player.lvl * Player.MaxExp) / 700)
        if Player.lvl < 10:
            Player.MaxExp += 50 * Player.lvl
            Player.MaxHP += 5 * Player.lvl
            Player.Strength += Player.lvl
        elif Player.lvl > 10 and Player.lvl < 30:
            Player.MaxExp += 50 * Player.lvl
        if Player.Pclass == 'swordsman':
            Player.MaxHP += ceil((Player.lvl / 7))
            Player.Strength += ceil((Player.lvl / 5))
            Player.Defense += ceil((Player.lvl / 10))
        elif Player.Pclass == 'wizard':
            Player.MaxHP += ceil((Player.lvl / 12))
            Player.Strength += ceil((Player.lvl / 2))
            Player.Defense += ceil((Player.lvl / 15))
        elif Player.Pclass == 'rouge':
            Player.MaxHP += ceil((Player.lvl / 10))
            Player.Strength += ceil((Player.lvl / 7))
            Player.Defense += ceil((Player.lvl / 12))
        Player.hp = Player.MaxHP
    if Player.lvl >= 100:
        print("You are max level")
        Player.exp = Player.MaxExp

#Introduction to the forest
def ForestIntro():
    if Player.hp > 0:
        print("Welcome to the forest!")
    elif Player.hp <= 0:
        if Player.gold <= 0 and CheckHealing() == False:
            Death()
        else:
            print("You do not have enough hp to fight.")
    else:
        print("ERROR: Can't Access forest")

#For the player to explore
def forest():
    ForestIntro()
    choice = " "
    random.seed()

    while choice != "5" and Player.hp != 0:
        print("1.up \n2.left \n3.right \n4.down \n5.exit")
        choice = input()
        print("")
        if choice >= "1" and choice <= "4":
            rand = random.randrange(0,2)
            if rand == 0:
                print("A group of trees")
            elif rand == 1:
                print("You encountered a monster")
                fight()
            else:
                print("ERROR")
        elif choice == "5":
            print("Leaving forest")
        else:
            print("Wrong choice")

#Function for healing facility for the game
def Healer():
    print("Welcome to the healer.\nWould you like to heal?")
    choice = input("Y/N\n")
    if Player.hp != Player.MaxHP and choice == 'Y' or choice == 'y':
        if Player.gold <= 0:
            print("You do not have any gold to heal!")
        elif Player.gold > 0:
            while Player.hp != Player.MaxHP and Player.gold > 0:
                Player.hp += 1
                Player.gold -= 1

            print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
        else:
            print("ERROR: Can not heal")
    elif choice == 'N' or choice == 'n':
        print("Thank you for visiting")
    else:
        print("Wrong choice")

def PrintEquip():
    for key in Player.Equipment:
        print(key)

#Displays the players stats
def PlayerStats():
    print("Name: " + Player.name)
    print("Level: " + str(Player.lvl))
    print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
    print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
    print("Strength: " + str(Player.Strength))
    print("Defense: " + str(Player.Defense))
    print("Gold: " + str(Player.gold))

    print("\nEquipment:")
    PrintEquip()

#Display a stat of a selected items
def ItemStats():
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

#Printing out store items
def PrintStore(Stype):
    for key, value in list(Items.items()):
        if (value[Item.Pclass] == Player.Pclass or  value[Item.Type] == 'item') and (value[Item.Type] == Stype):
            if value[Item.lvl] >= Player.lvl and value[Item.lvl] <= (Player.lvl + 5):
                print(key + ": " + str(value[Item.price]))

#The main function for buying a weapon, armor, or item
def Mbuy(Stype):
    PrintStore(Stype)
    print("Type the name of the " + Stype + " you want to buy or no to exit")
    item_name = input()
    if item_name == 'no':
        print("Thank you for shopping with us")
    elif item_name != 'no':
        price = 0
        ItemType = ''

        if ItemCheck(item_name) == True:
            price = Items[item_name][Item.price]
            ItemType = Items[item_name][Item.Type]

        if price != 0 and ItemType != '':
            if Player.gold >= price:
                Player.gold -= price
                if ItemType != 'item':
                    print("Do you want to equip the " + item_name + ": yes/no")
                    choice = input()
                    if choice == 'yes':
                        EquipInsert(item_name)
                        if Items[item_name][Item.lvl] > Player.lvl:
                            InvenInsert(item_name)
                            print("The item has been put in your inventory")
                    elif choice == 'no':
                        InvenInsert(item_name)
                    else:
                        print("ERROR: Could not put away or equip " + item_name)
                elif ItemType == 'item':
                    print("Item put in your inventory.")
                    InvenInsert(item_name)
                else:
                    print("ERROR: Something went wrong with buying item")
            else:
                print("You do not have enough money")

        elif price == 0 and ItemType != '':
            print("Unidentified item")
        else:
            print("ERROR: can't buy item")

#Function for buying store items
def Buy():
    buy = ""

    while buy != '4':
        print("1.Weapon \n2.Armor \n3.Item \n4.Exit")
        buy = input()
        if buy == '1':
            Mbuy('weapon')
        elif buy == '2':
            Mbuy('armor')
        elif buy == '3':
            Mbuy('item')
        elif buy == '4':
            print("Thank you for shopping with us")
            break;
        else:
            print("ERROR: could not buy item")

#Function for selling store items
def Sell():
    sell = ""
    while sell != "exit":
        PrintInven()
        print("What item do you want to sell from your inventory?")
        print("Type exit to go back")
        sell = input()

        for key, value in list(Player.Inventory.items()):
            if key == sell:
                Igold = ceil((value[Item.price] * .8))
                if value[Item.count] > 1:
                    Player.gold += Igold
                    value[Item.count] -= 1
                    print(value[Item.count])
                    print("You gained " + str(Igold) + " gold.")
                elif value[Item.count] == 1:
                    Player.gold += Igold
                    value[Item.count] -= 1
                    print("You gained " + str(Igold) + " gold.")
                    del Player.Inventory[sell]
                else:
                    print("ERROR: Can't sell item")

#Prints items in inventory that can be sold
def PrintInven():
    for key, value in list(Player.Inventory.items()):
        print(key + " X " + str(value[Item.count]))
        
#The store for the player
def Store():
    print("1.Buy \n2.Sell \n3.Exit")
    choice = input()
    if choice == "1":
        Buy()
    elif choice == "2":
        Sell()
    elif choice == "3":
        print("Thanks for shopping")
    else:
        print("Wrong choice")

#Displays the players inventory
def DisplayInventory():
    choice = ''
    while choice != '4':
        PrintInven()

        print("\n1. Equip a weapon or armor")
        print("2. Use an item")
        print("3. Exit")

        choice = input()

        if choice == '1':
            print("Enter the name of the weapon/armor")
            Equip = input()
            CheckItem = InvenCheck(Equip)
            if bool(CheckItem) == True:
                EquipInsert(Equip)
            elif bool(CheckItem) == False:
                print("Weapon/armor not in inventory")
            else:
                print("ERROR: can not equip item from inventory")
        elif choice == '2':
            print("Enter the name of the item to use")
            item_name = input()
            CheckItem = InvenCheck(item_name)
            if bool(CheckItem) == True:
                for key, value in list(Player.Inventory.items()):
                    if key == item_name:
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
        elif choice == '3':
            print("Exiting inventory")
            choice = '4'

#Checks if item is in player inventory
def InvenCheck(item_name):
    for key, value in list(Player.Inventory.items()):
        if key == item_name:
            return True
    return False

def EquipCheck(item_name):
    for key, value in list(Player.Equipment.items()):
        if key == item_name:
            return True
    return False

def ItemCheck(item_name):
    for key, value in list(Items.items()):
        if key == item_name:
            return True
    return False

def EquipTypeCheck(Etype):
    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == Etype:
            return True
    return False

#Exiting the game
def Exit():
    return True

def DeathCheck():
    if Player.gold <= 0 and CheckHealing() == False:
        Death()

#Main menu for the game. The player can choose what to do and where to go.
def Choices():
    stop = False;
    while stop == False:
        DeathCheck()
        print("\n1.Forest \n2.Healer \n3.Player Stats \n4.Inventory")
        print("5.Item Stats \n6.Store \n7.Exit")
        choice = input()
        print("")
        if choice == "1":
            forest()
        elif choice == "2":
            Healer()
        elif choice == "3":
            PlayerStats()
        elif choice == "4":
            DisplayInventory()
        elif choice == "5":
            ItemStats()
        elif choice == "6":
            Store()
        elif choice == "7":
            stop = Exit()
        else:
            print("Wrong Choice")

#Main game function
def main():
    GameIntro()
    Choices()

if __name__ == '__main__':
    main()
