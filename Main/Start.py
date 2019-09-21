import os
from Classes.Classes import Player

try:
    import _pickle as pickle
except ImportError:
    print("Can't open saved file without _pickle import")

def Start():
    '''Loads in the players stats when the game is opened'''

    playerFilePath = '../Player/PlayerFile.txt'
    equipmentFilePath = '../Player/Equipment.txt'
    inventoryFilePath = '../Player/Inventory.txt'

    if os.path.isfile(playerFilePath):
        if os.stat(playerFilePath).st_size != 0:

            with open(playerFilePath) as f:
                Player.name = f.readline()
                Player.MaxHP = f.readline()
                Player.hp = f.readline()
                Player.Strength = f.readline()
                Player.Defense = f.readline()
                Player.gold = f.readline()
                Player.MaxExp = f.readline()
                Player.exp = f.readline()
                Player.lvl = f.readline()
                Player.Pclass = f.readline()

            Player.name = Player.name.strip('\n')
            Player.MaxHP = int(Player.MaxHP)
            Player.hp = int(Player.hp)
            Player.Strength = int(Player.Strength)
            Player.Defense = int(Player.Defense)
            Player.gold = int(Player.gold)
            Player.MaxExp = int(Player.MaxExp)
            Player.exp = int(Player.exp)
            Player.lvl = int(Player.lvl)
            Player.Pclass = Player.Pclass.strip('\n')

    if os.path.isfile(equipmentFilePath):
        if os.stat(equipmentFilePath).st_size != 0:
            with open(equipmentFilePath, 'rb') as f:
                Player.Equipment = pickle.load(f)

    if os.path.isfile(inventoryFilePath):
        if os.stat(inventoryFilePath).st_size != 0:
            with open(inventoryFilePath, 'rb') as f:
                Player.Inventory = pickle.load(f)
