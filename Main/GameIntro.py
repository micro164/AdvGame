from Player.Inventory import inventory_insert
from Classes.Classes import Player
from Utilities.Checks import name_check
from Player.Equipment import equip_insert
from Utilities.HelperUtilities import print_text
from Utilities.HelperUtilities import print_slow
import uuid


def game_intro():
    """Introduction to the game"""

    if Player.Pclass == "":
        print_slow("Welcome to TxtBasedAdv")
        print_slow("Please enter a name: ", 0.025)
        Player.name = input()
        name_check(Player.name)
        print_slow("Hello " + Player.name)

        print_slow("\nChoose your class", 0.025)
        print_slow("1.Swordsman Class \n2.Wizard Class \n3.Rogue Class", 0.025)
        Player.uniqueId = uuid.uuid1().int
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
        intro()
    else:
        print("GameIntro went wrong!!")


def intro():
    """Another part to the game introduction"""

    inventory_insert('potion')

    print_slow("Now you are ready to go on an adventure. You will be able to travel", 0.025)
    print_slow("and collect awesome items and level up to your hearts content.", 0.025)


def _assign_class(PlayerClass, strength, dfs, hp, mHp, weapon, armor):
    """Assigning the players class and stats

    Arguments:
    PlayerClass - The class the player chose
    str - Starting strength of the player
    dfs - Starting defense of the player
    hp - Starting hp of the player
    mHp - Starting MaxHP of the player
    weapon - Starting weapon of the player
    armor - Starting armor of the player

    """

    print_slow("\nWelcome to the " + PlayerClass + " class")
    Player.Pclass = PlayerClass
    Player.Strength = strength
    Player.Defense = dfs
    Player.hp = hp
    Player.MaxHP = mHp
    equip_insert(weapon)
    print_text("You have been given a " + weapon)
    equip_insert(armor)
    print_text("You have been given a " + armor + ".\n")
    intro()
