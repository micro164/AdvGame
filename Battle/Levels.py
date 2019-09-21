from Classes.Classes import Player

from math import ceil
from math import floor

def LevelUp():
    '''Checks if the player can reach a new level and then adds the stats to the player'''

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
        elif Player.lvl > 10 and Player.lvl < 30:
            Player.MaxExp += 50 * Player.lvl
            if Player.Pclass == 'swordsman':
                _lowLevelUp(7, 5, 10)
            elif Player.Pclass == 'wizard':
                _lowLevelUp(12, 2, 15)
            elif Player.Pclass == 'rouge':
                _lowLevelUp(10, 7, 12)
        elif Player.lvl >= 30 and Player.lvl < 100:
             if Player.Pclass == 'swordsman':
                 _highLevelUp(1000, 5, 5, 7)
             elif Player.Pclass == 'wizard':
                 _highLevelUp(1000, 10, 2, 10)
             elif Player.Pclass == 'rouge':
                 _highLevelUp(500, 8, 7, 10)
        Player.hp = Player.MaxHP
    if Player.lvl >= 100:
        print("You are max level")
        Player.exp = Player.MaxExp

def _lowLevelUp(hpDivision, strDivision, dfsDivision):
    Player.MaxHP += ceil((Player.lvl / hpDivision))
    Player.Strength += ceil((Player.lvl / strDivision))
    Player.Defense += ceil((Player.lvl / dfsDivision))

def _highLevelUp(exp, hpDivision, strDivision, dfsDivision):
    expDivision = (stringToInt(Player.PClass) / len(Player.PClass))

    Player.MaxExp += ceil((exp * Player.lvl) / expDivision)
    Player.MaxHP += ceil((Player.lvl / hpDivision))
    Player.Strength += ceil((Player.lvl / strDivision))
    Player.Defense += ceil((Player.lvl / dfsDivision))

def stringToInt(string):
    value = 0

    for c in string:
        value += ord(c)
