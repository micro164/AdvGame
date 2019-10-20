from Classes.Classes import Player

from math import ceil
from math import floor


def level_up():
    """Checks if the player can reach a new level and then adds the stats to the player"""

    while Player.exp >= Player.MaxExp and Player.lvl < 100:
        print("YOU LEVELED UP!!!!!")
        Player.lvl += 1
        print("You are now level " + str(Player.lvl))
        Player.MaxExp += floor((Player.lvl * Player.MaxExp) / 700)
        if Player.lvl < 10:
            Player.MaxExp += 50 * Player.lvl
            Player.MaxHP += 5 * Player.lvl
            Player.Strength += Player.lvl
            Player.Defense += Player.lvl
        elif 10 < Player.lvl < 30:
            Player.MaxExp += 50 * Player.lvl
            if Player.Pclass == 'swordsman':
                _low_level_up(7, 5, 10)
            elif Player.Pclass == 'wizard':
                _low_level_up(12, 2, 15)
            elif Player.Pclass == 'rouge':
                _low_level_up(10, 7, 12)
        elif 30 <= Player.lvl < 100:
            if Player.Pclass == 'swordsman':
                _high_level_up(1000, 5, 5, 7)
            elif Player.Pclass == 'wizard':
                _high_level_up(1000, 10, 2, 10)
            elif Player.Pclass == 'rouge':
                _high_level_up(500, 8, 7, 10)
        Player.hp = Player.MaxHP
    if Player.lvl >= 100:
        print("You are max level")
        Player.exp = Player.MaxExp


def _low_level_up(hp_division, str_division, dfs_division):
    Player.MaxHP += ceil((Player.lvl / hp_division))
    Player.Strength += ceil((Player.lvl / str_division))
    Player.Defense += ceil((Player.lvl / dfs_division))


def _high_level_up(exp, hp_division, str_division, dfs_division):
    exp_division = (string_to_int(Player.PClass) / len(Player.PClass))

    Player.MaxExp += ceil((exp * Player.lvl) / exp_division)
    Player.MaxHP += ceil((Player.lvl / hp_division))
    Player.Strength += ceil((Player.lvl / str_division))
    Player.Defense += ceil((Player.lvl / dfs_division))


def string_to_int(string):
    value = 0

    for c in string:
        value += ord(c)
