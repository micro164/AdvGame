#!/usr/bin/python3

#Author: Jonathon Bryant
#Date Created: 9/22/17
#Date Modified: 12/17/17
#This is a simple text based game created in the language of python

#-----------------------IMPORTS-----------------------------

from enum import IntEnum

#-----------------------ITEMS-------------------------------

Items = {'sword': list((10,0,10,'weapon', 'swordsman', 0,0,1)),
         'wand': list((5,0,2,'weapon','wizard',0,0,1)),
         'dagger': list((7,0,5,'weapon','rouge',0,0,1)),
         'bronze armor': list((0,10,10,'armor','swordsman',0,0,1)),
         'cloth armor': list((0,5,2,'armor','wizard',5,0,1)),
         'hard cloth armor': list((0,7,5,'armor','rouge',0,0,1)),
         'potion': list((0,0,20,'item', 'none', 20,0,1)),
         'test': list((0,0,0,'weapon','swordsman',0,0,0))}

#------------------------MONSTERS----------------------------

Monsters = {'rat': list((50,5,2))}

#------------------------CLASSES-----------------------------

#Player stats
class Player:
    name = ""
    MaxHP = 0
    hp = 0
    Strength = 0
    Defense = 0
    gold = 0
    lvl = 1
    Pclass = ""
    Inventory = dict()
    Equipment = dict()

#Monster Class
class Monster(IntEnum):
    HP = 0
    attack = 1
    defense = 2

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
    for key, value in list(Player.Equipment.items()):
        if value[Item.Type] == Etype and value[Item.count] != 0:
            Player.Strength -= value[Item.attack]
            Player.Defense -= value[Item.defense]
            Player.MaxHP -= value[Item.HP]
            #value[Item.count] -= 1
            del Player.Equipment[key]

#Removing Equipment
def RemoveEquip(item_name):
    if bool(Player.Equipment) != False:
        for key, value in list(Items.items()):
            if key == item_name and Player.Pclass == value[Item.Pclass]:
                if value[Item.Type] == 'weapon':
                    DeleteEquip('weapon')
                elif value[Item.Type] == 'armor':
                    DeleteEquip('armor')
                else:
                    print("ERROR: can't remove equipment")

#Inserting Item into equipment
def EquipInsert(item_name):
    RemoveEquip(item_name)

    for key, value in list(Items.items()):
        if key == item_name and Player.Pclass == value[Item.Pclass]:
            Player.Equipment[item_name] = Items[item_name]
            for key2, value2 in list(Player.Equipment.items()):
                if key2 == item_name:
                    Player.Strength += value2[Item.attack]
                    Player.Defense += value2[Item.defense]
                    Player.MaxHP += value2[Item.HP]
                    value2[Item.count] += 1

#Inserting Item into inventory
def InvenInsert(item_name):
    Player.Inventory[item_name] = Items[item_name]

    Echeck = False

    for key in Player.Equipment:
        if key == item_name:
            Echeck = True

    for key, value in list(Player.Inventory.items()):
        if key == item_name and Echeck == False:
            value[Item.count] += 1

#Game Intro
def GameIntro():
    print("Welcome to TxtBasedAdv")
    print("Please enter a name: ")
    Player.name = input()
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
        print("You have been given a " + list(Player.Equipment)[0])
        EquipInsert('bronze armor')
        print("You have been given a " + list(Player.Equipment)[1] + "\n")
    elif choice == "2":
        print("Welcome to the wizard class\n")
        Player.Pclass = 'wizard'
        Player.Strength = 5
        Player.Defense = 3
        Player.hp = 50
        Player.MaxHP = 50
        EquipInsert('wand')
        print("You have been given a " + list(Player.Equipment)[0])
        EquipInsert('cloth armor')
        print("You have been given a " + list(Player.Equipment)[1] + "\n")
    elif choice == "3":
        print("Welcome to the rogue class\n")
        Player.Pclass = 'rouge'
        Player.Strength = 7
        Player.Defense = 5
        Player.hp = 70
        Player.MaxHP = 70
        EquipInsert('dagger')
        print("You have been given a " + list(Player.Equipment)[0])
        EquipInsert('hard cloth armor')
        print("You have been given a " + list(Player.Equipment)[1] + "\n")
    else:
        print("Wrong choice")

    InvenInsert('potion')
    InvenInsert('sword')

    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")

#def forest():

#Function for healing facility for the game
def Healer():
    print("Welcome to the healer.\Would you like to heal?")
    choice = input("Y/N\n")
    if Player.hp != Player.MaxHP and choice == 'Y' or choice == 'y':
        Player.hp = Player.MaxHP

#Displays the players stats
def PlayerStats():
    print("Name: " + Player.name)
    print("Level: " + str(Player.lvl))
    print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
    print("Strength: " + str(Player.Strength))
    print("Defense: " + str(Player.Defense))
    print("Gold: " + str(Player.gold))

    print("\nEquipment:")
    for key in Player.Equipment:
        print(key)

#Display a stat of a selected items
def ItemStats():
    print("What item do you want to look up?")
    item_lookup = input()

    for key, value in list(Items.items()):
        if key == item_lookup:
            print("Name: " + key)
            print("Attack: " + str(value[Item.attack]))
            print("Defense: " + str(value[Item.defense]))
            print("HP: " + str(value[Item.HP]))
            print("Price: " + str(value[Item.price]))
            print("Type: " + value[Item.Type])
            print("Class: " + value[Item.Pclass])

#Printing out store items
def PrintStore(Stype):
    for key, value in list(Item.items()):
        if value[Item.Pclass] == Player.Pclass and value[Item.Type] == Stype:
            if value[Item.lvl] >= Player.lvl and value[Item.lvl] <= (Player.lvl + 5):
                print(key + ": " + str(value[Item.price]))

#Function for buying store items
def Buy():
    print("1.Weapon \n2.Armor \n3.Item")
    buy = input()
    if buy == "1":
        PrintStore('weapon')
        print("Type the name of the item you want to buy")
        weapon = input()
        Player.gold -= value[Item.price]
        print("Do you want to equip the weapon")
        choice = input()
        if choice == 'yes':
            EquipInsert(weapon)
        elif choice == 'no':
            InvenInsert(weapon)
        else:
            print("ERROR: Could not buy item")

#Function for selling store items
def Sell():
    print("What item do you want to sell from your inventory?")
    sell = input()

    for key, value in list(Player.Inventory.items()):
        if key == sell:
            if value[Item.count] > 1:
                Player.gold += (value[Item.price] * .8)
                value[Item.count] -= 1
            elif value[Item.count] == 1:
                Player.gold += (value[Item.price] * .8)
                value[Item.count] -= 1
                del Player.Inventory[sell]

#The store for the player
def Store():
    print("1.Buy \n2.Sell")
    choice = input()
    if choice == "1":
        Buy()
    elif choice == "2":
        Sell()
    else:
        print("Wrong choice")

#Displays the players inventory
def DisplayInventory():
    for key, value in list(Player.Inventory.items()):
        print(key + " X " + str(value[Item.count]))

#Exiting the game
def Exit():
    return True

#Main menu for the game. The player can choose what to do and where to go.
def Choices():
    stop = False;
    while stop == False:
        print("\n1.Forest \n2.Healer \n3.Player Stats \n4.Inventory")
        print("5.Item Stats \n6.Store \n7.Exit")
        choice = input()
        if choice == "1":
            print("Not ready yet")
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
