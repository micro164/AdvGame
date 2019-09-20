from Inventory import InvenInsert
from Classes import Player
from Checks import NameCheck
from Equipment import EquipInsert

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

        if choice == "1":
            _AssignClass("swordsman", 10, 10, 100, 100, 'sword', 'bronze armor')
        elif choice == "2":
            _AssignClass("wizard", 5, 3, 50, 50, 'wand', 'cloth armor')
        elif choice == "3":
            _AssignClass("rogue", 7, 5, 70, 70, 'dagger', 'hard cloth armor')
        else:
            print("Wrong choice")
            GameIntro()
    elif Player.Pclass != "":
        Intro()
    else:
        print("GameIntro went wrong!!")

def Intro():
    '''Another part to the game introduction'''

    InvenInsert('potion')

    print("Now you are ready to go on an adventure. You will be able to travel")
    print("and collect awsome items and level up to your hearts content.\n")

def _AssignClass(PlayerClass, str, dfs, hp, mHp, weapon, armor):
    '''Assigning the players class and stats

    Arguments:
    PlayerClass - The class the player chose
    str - Starting strength of the player
    dfs - Starting defense of the player
    hp - Starting hp of the player
    mHp - Starting MaxHP of the player
    weapon - Starting weapon of the player
    armor - Starting armor of the player

    '''

    print("Welcome to the " + PlayerClass + " class\n")
    Player.Pclass = PlayerClass
    Player.Strength = str
    Player.Defense = dfs
    Player.hp = hp
    Player.MaxHP = mHp
    EquipInsert(weapon)
    print("You have been given a " + weapon)
    EquipInsert(armor)
    print("You have been given a " + armor + ".\n")
    Intro()
