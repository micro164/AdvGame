from InventoryAndItems import InvenInsert
from Classes import Player
from Checks import NameCheck
from Equipment import EquipInsert

#Game Intro
def GameIntro():
    '''Introduction to the game'''

    if Player.Pclass == "":
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
            InvenInsert('sword')
            print("You have been given a sword.")
            EquipInsert('bronze armor')
            InvenInsert('bronze armor')
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
    elif Player.Pclass != "":
        Intro()
    else:
        print("GameIntro went wrong!!")

#Gives the player a potion to survive and an awsome introduction to the game
def Intro():
    '''Another part to the game introduction'''

    InvenInsert('potion')

    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")
