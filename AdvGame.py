#!/usr/bin/python3

#Author: Jonathon Bryant
#Date: 9/22/17
#This is a simple text based game created in the language of python

#-----------------------IMPORTS-----------------------------

from collections import namedtuple
from collections import defaultdict
from enum import IntEnum

#-----------------------ITEMS-------------------------------

Item = namedtuple('Item', ('attack', 'defence', 'price', 'Type', 'Pclass', 'HP'))
Items = {
    'sword': Item(10,0,10,'weapon','swordsman',0),
    'wand': Item(5,0,2,'weapon', 'swordsman',0),
    'dagger': Item(7,0,5,'weapon', 'rouge',0),
    'potion': Item(0,0,20,'healer', 'none', 20)
}

Weapons = {'sword': list((10,0,10,'weapon', 'swordsman', 0)),
           'wand': list((5,0,2,'weapon','wizard',0)),
           'dagger': list((7,0,5,'weapon','rouge',0))}

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

#Weapon Class
class Weapon(IntEnum):
    attack = 0
    defense = 1
    price = 2
    Type = 3
    Pclass = 4
    HP = 5

#-----------------------FUNCTIONS-----------------------------

#Inserting Item into equipment
def EquipInsert(item_name):
    ItemsIndex = 0
    for key, value in list(Items.items()):
        if key == item_name:
            itemClass = value.Pclass
            Player.Strength += value.attack
            Player.Defense += value.defence
            Index = ItemsIndex
        ItemsIndex += 1
    
    for key in Items:
        if key == item_name and Player.Pclass == itemClass:
            Player.Equipment = list(Items.items())[Index]
            ItemsIndex += 1

#Inserting Item into inventory
def InvenInsert(item_name):
    index = 0
    firstItem = 0
        
    for key, value in list(Items.items()):
        if key == item_name and firstItem > 0:
            Player.Inventory[item_name] = list(Items.items())[index]
        elif firstItem == 0:
            Player.Inventory[0] = list(Items.items())[index]
            firstItem += 1           
        index += 1
        
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
        print("You have been given a " + Player.Equipment[0] + "\n")
    elif choice == "2":
        print("Welcome to the wizard class\n")
        Player.Pclass = 'wizard'
        Player.Strength = 5
        Player.Defense = 3
        Player.hp = 50
        Player.MaxHP = 50
        EquipInsert('wand')
        print("You have been given a " + Player.Equipment[0] + "\n")
    elif choice == "3":
        print("Welcome to the rogue class\n")
        Player.Pclass = 'rouge'
        Player.Strength = 7
        Player.Defense = 5
        Player.hp = 70
        Player.MaxHP = 70
        EquipInsert('dagger')
        print("You have been given a " + Player.Equipment[0] + "\n")
    else:
        print("Wrong choice")

    InvenInsert('potion')
    InvenInsert('wand')

    for key, value in list(Weapons.items()):
        print(key, value)
        print(value[Weapon.Type])
        print(type(value))
        
    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")
        
#def forest():
    
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
    for i in range(len(Player.Equipment)):
        if i%2 == 0:
            print(Player.Equipment[i])

def DisplayInventory():
##    for key, value in list(Player.Inventory):
##        print(key + ": " + value.count)
    print(Player.Inventory[0])
    #print(Player.Equipment)
        
#Exiting the game
def Exit():
    return True
        
  #Choices
def Choices():
    stop = False;
    while stop == False:
        print("\n1.Forest \n2.Healer \n3.Player Stats \n4.Inventory")
        print("5.Exit")
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
            stop = Exit()
        else:
            print("Wrong Choice")
        
    
#Main game function
def main():
    GameIntro()
    Choices()

if __name__ == '__main__':
    main()
