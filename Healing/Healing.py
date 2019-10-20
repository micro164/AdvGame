from Classes.Classes import Player
from Utilities.HelperUtilities import PrintSlow


def healer():
    """Gives the player a choice to heal in exchange for gold"""

    PrintSlow("Welcome to the healer.\nWould you like to heal?")
    choice = input("Y/N\n")
    if Player.hp != Player.MaxHP and choice == 'Y' or choice == 'y':
        _check_player_healing()
    elif choice == 'N' or choice == 'n':
        print("Thank you for visiting")
    else:
        print("Wrong choice")


def _check_player_healing():
    if Player.gold <= 0:
        print("You do not have any gold to heal!")
    elif Player.gold > 0:
        _heal_player()
    else:
        print("ERROR: Can not heal")


def _heal_player():
    while Player.hp != Player.MaxHP and Player.gold > 0:
        Player.hp += 1
        Player.gold -= 1

    print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
