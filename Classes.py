from enum import IntEnum
from enum import Enum

#Player stats
class Player:
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

#Monster Class
class Monster(IntEnum):
    HP = 0
    attack = 1
    defense = 2
    exp = 3
    lvl = 4
    MaxHP = 5

#Item Class
class Item(IntEnum):
    attack = 0
    defense = 1
    price = 2
    Type = 3
    Pclass = 4
    HP = 5
    count = 6
    lvl = 7

class Directions(Enum):
    UP = '1'
    LEFT = '2'
    RIGHT = '3'
    DOWN = '4'

class Features():
    choiceList = []
    LastDirections = []

class QuestInfo():
    MonstersKilled = dict()
    QuestNumber = 2
    QuestSeen = False
    Win = True
    InQuest = False
