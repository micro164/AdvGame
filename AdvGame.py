#!/usr/bin/python3

#Author: Jonathon Bryant
#Date: 9/22/17
#This is a simple text based game created in the language of python

#-----------------------IMPORTS-----------------------------
from collections import namedtuple

Item = namedtuple('Item', ('attack', 'defence', 'price', 'Type', 'Pclass'))
Items = {
    'sword': Item(10,0,10,'weapon','swordsman'),
    'wand': Item(5,0,2,'weapon', 'wizard'),
    'dagger': Item(7,0,5,'weapon', 'rouge')
}

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
    Inventory = {}
    Equipment = dict()

#-----------------------FUNCTIONS-----------------------------

#Inserting Item into equipment
def EquipInsert(item_name):
    ItemsIndex = 0
    for key, value in list(Items.items()):
        if key == item_name:
            itemClass = value.Pclass
            Index = ItemsIndex
        ItemsIndex += 1
    
    for key in Items:
        if key == item_name and Player.Pclass == itemClass:
            Player.Equipment = list(Items.items())[Index]
            ItemsIndex += 1
        
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
        EquipInsert('wand')
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
        
    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")
        
#def forest():
    
def Healer():
    print("Welcome to the healer.\Would you like to heal?")
    choice = input("Y/N\n")
    if Player.hp != Player.MaxHP and choice == 'Y' or choice == 'y':
        Player.hp = Player.MaxHP
        
#Exiting the game
def Exit():
    return True
        
#Choices
def Choices():
    stop = False;
    while stop == False:
        print("\n1.Forest \n2.Healer \n3.Exit")
        choice = input()
        if choice == "1":
            print("Not ready yet")
        elif choice == "2":
            Healer()
        elif choice == "3":
            stop = Exit()
        else:
            print("Wrong Choice")
        
    
#Main game function
def main():
    GameIntro()
    Choices()

if __name__ == '__main__':
    main()
