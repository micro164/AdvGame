from Player.Inventory import InvenInsert
from Classes.Classes import Player
from Utilities.Checks import NameCheck
from Player.Equipment import EquipInsert
from Utilities.HelperUtilities import Print
from Utilities.HelperUtilities import PrintSlow
import uuid


def game_intro():
    '''Introduction to the game'''

    if Player.Pclass == "":
        PrintSlow("Welcome to TxtBasedAdv")
        PrintSlow("Please enter a name: ", 0.05)
        Player.name = input()
        NameCheck(Player.name)
        PrintSlow("Hello " + Player.name)

        PrintSlow("\nChoose your class", 0.05)
        PrintSlow("1.Swordsman Class \n2.Wizard Class \n3.Rogue Class", 0.05)
        choice = input()

        if choice == "1":
            _assign_class("swordsman", 10, 10, 100, 100, 'sword', 'bronze armor')
        elif choice == "2":
            _assign_class("wizard", 5, 3, 50, 50, 'wand', 'cloth armor')
        elif choice == "3":
            _assign_class("rogue", 7, 5, 70, 70, 'dagger', 'hard cloth armor')
        else:
            print("Wrong choice")
            game_intro()
    elif Player.Pclass != "":
        Player.uniqueId = uuid.uuid1().int
        intro()
    else:
        print("GameIntro went wrong!!")


def intro():
    '''Another part to the game introduction'''

    InvenInsert('potion')

    PrintSlow("Now you are ready to go on an adventure. You will be able to travel", 0.05)
    PrintSlow("and collect awsome items and level up to your hearts content.", 0.05)


def _assign_class(PlayerClass, str, dfs, hp, mHp, weapon, armor):
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

    PrintSlow("\nWelcome to the " + PlayerClass + " class")
    Player.Pclass = PlayerClass
    Player.Strength = str
    Player.Defense = dfs
    Player.hp = hp
    Player.MaxHP = mHp
    EquipInsert(weapon)
    Print("You have been given a " + weapon)
    EquipInsert(armor)
    Print("You have been given a " + armor + ".\n")
    intro()
