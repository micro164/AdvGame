from Classes.Classes import Player
from Utilities.Checks import check_healing


def death():
    """Revives the player when there is no other way to gain hp"""

    if Player.hp == 0 and Player.gold == 0:
        healing_item = check_healing()
        check_healing_options(healing_item)


def death_check():
    """Checks if the player has no other options to heal"""

    if Player.gold <= 0 and check_healing() is False:
        death()


def check_healing_options(is_healing_item):
    """Figures out which healing option the player has"""

    if bool(is_healing_item) == False and Player.exp > 0:
        no_money_healing()
    elif Player.exp == 0 and bool(is_healing_item) == False:
        no_money_and_exp_healing()


def no_money_healing():
    """Heals the player when they have no money"""

    print("Grim Reaper: 'You have no gold to heal yourself. Muhahaha'")
    print("Grim Reaper: 'I will take some experience from you in order to restore your life.'")
    print("")
    Player.exp -= 10 * Player.lvl
    if Player.exp < 0:
        Player.exp = 0
    Player.hp = Player.MaxHP


def no_money_and_exp_healing():
    """Heals the player when they have no money or experience"""

    print("Grim Reaper: 'You have nothing so I will add to your Max Exp. to restore your life.'")
    print("")
    Player.MaxExp += 10 * Player.lvl
    Player.hp = Player.MaxHP
