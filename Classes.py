from enum import IntEnum
from enum import Enum

class Player:
    '''Player Class'''
    name = ""
    MaxHP = 0
    hp = 0
    Strength = 0
    Defense = 0
    gold = 0
    MaxExp = 100
    exp = 0
    lvl = 1
    Pclass = ""
    Inventory = dict()
    Equipment = dict()

class Monster(IntEnum):
    '''Monster Class'''
    HP = 0
    attack = 1
    defense = 2
    exp = 3
    lvl = 4
    MaxHP = 5

class enemy(object):
    """Enemy class"""
    name = ""
    HP = 0
    attack = 0
    defense = 0
    exp = 0
    lvl = 0
    MaxHP = 0
    questFight = False

    def __init__(self, name='', hp=0, attack=0, defense=0, exp=0, lvl=0, maxHp=0, questFight=False):
        super(enemy, self).__init__()
        self.name = name
        self.HP = hp
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.lvl = lvl
        self.MaxHP = maxHp
        self.questFight = questFight

class Item(IntEnum):
    '''Item Class'''
    attack = 0
    defense = 1
    price = 2
    Type = 3
    Pclass = 4
    HP = 5
    count = 6
    lvl = 7

class Directions(Enum):
    '''Directions Class'''
    UP = '1'
    LEFT = '2'
    RIGHT = '3'
    DOWN = '4'

class Features():
    '''Features Class'''
    choiceList = []
    LastDirections = []

class QuestInfo():
    '''QuestInfo Class'''
    MonstersKilled = dict()
    QuestNumber = 0
    QuestSeen = False
    Win = True
    InQuest = False
