from Classes.Classes import Player
from Classes.Classes import Monster

#Stats for monsters
# 0-HP, 1-attack, 2-defense, 3-exp, 4.lvl, 5.MaxHP
Monsters = {'rat':              list((50,   12,      7,      10,     1,   50)),
            'Wild Chicken':     list((40,   10,      5,      5,      1,   10)),
            'Spider':           list((65,   15,     10,      15,     3,   25)),
            'goblin':           list((80,  17,     7,      35,     5,   100)),
            'Giant Spider':     list((110,   25,     15,     75,     10,  75)),
            'Giant Rat':        list((130,  40,     35,     100,    12,  100)),
            'Armored Goblin':   list((150,  80,     45,     125,    15,  150)),
            'Zombie':           list((250,  100,     30,     150,    17,  250)),
            'Goblin Zombie':    list((400,  155,     50,     200,    20,  400)),
            'Wolf':             list((350,  195,     55,     190,    23,  200)),
            'Undead Wolf':      list((600,  220,     60,     250,    25,  400)),
            'Ghost':            list((800,  250,     65,     225,    30,  500)),
            'Ghoul':            list((825,  260,     70,     300,    35,  425)),
            'Vampire':          list((950,  290,     80,     500,    40,  650)),
            'Cyclops':          list((1200,  280,     130,    525,    45,  700)),
            'Mummy':            list((1675,  285,     265,     550,    50,  675)),
            'Earth Elemental':  list((1800,  270,     280,    700,    55,  800)),
            'Wind Elemental':   list((1750,  240,     290,    700,    55,  750)),
            'Fire Elemental':   list((1710,  220,    210,    700,    55,  710)),
            'Water Elemental':  list((1850,  280,     400,    700,    55,  850)),
            'Basilisk':         list((1900,  300,    490,     800,    60,  900)),
            'Angel':            list((2000, 320,    700,    1000,   65,  1000)),
            'Griffon':          list((2125, 350,    725,    1300,   70,  1125)),
            'Baby Dragon':      list((2500, 400,    775,    2000,   75,  1500)),
            'Ifrit':            list((2700, 450,    750,    1800,   80,  1700)),
            'Phoenix':          list((4000, 475,    850,    2400,   85,  2000)),
            'Adamantoise':      list((4000, 500,    900,    2200,   90,  3000)),
            'Elder Lich':       list((4500, 800,    975,    2500,   95,  3500)),
            'Dragon':           list((10000, 1200,    1100,    5000,   100, 5000))}

def MonsterList():
    '''Gives a list of monsters that the player can fight'''

    temp = {}

    for key, value in list(Monsters.items()):
        if Player.lvl == 100:
            if value[Monster.lvl] <= Player.lvl:
                temp[key] = Monsters[key]
        elif value[Monster.lvl] >= 1 and value[Monster.lvl] <= (Player.lvl + 5):
            temp[key] = Monsters[key]
    return temp
