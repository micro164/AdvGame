from Classes import Player

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
        elif Player.lvl > 10 and Player.lvl < 30:
            Player.MaxExp += 50 * Player.lvl
        if Player.Pclass == 'swordsman':
            Player.MaxHP += ceil((Player.lvl / 7))
            Player.Strength += ceil((Player.lvl / 5))
            Player.Defense += ceil((Player.lvl / 10))
        elif Player.Pclass == 'wizard':
            Player.MaxHP += ceil((Player.lvl / 12))
            Player.Strength += ceil((Player.lvl / 2))
            Player.Defense += ceil((Player.lvl / 15))
        elif Player.Pclass == 'rouge':
            Player.MaxHP += ceil((Player.lvl / 10))
            Player.Strength += ceil((Player.lvl / 7))
            Player.Defense += ceil((Player.lvl / 12))
        Player.hp = Player.MaxHP
    if Player.lvl >= 100:
        print("You are max level")
        Player.exp = Player.MaxExp
