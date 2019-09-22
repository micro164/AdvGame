import os
from Classes.Classes import Player

try:
    import _pickle as pickle
except ImportError:
    print("Can't open saved file without _pickle import")

def Start():
    '''Loads in the players stats when the game is opened'''

    player_file_path = '../Player/PlayerFile.txt'
    equipment_file_path = '../Player/Equipment.txt'
    inventory_file_path = '../Player/Inventory.txt'

    if os.path.isfile(player_file_path):
        if os.stat(player_file_path).st_size != 0:

            with open(player_file_path) as f:
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
                Player.uniqueId = f.readline()

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
            Player.uniqueId = int(Player.uniqueId)

    if os.path.isfile(equipment_file_path):
        if os.stat(equipment_file_path).st_size != 0:
            with open(equipment_file_path, 'rb') as f:
                Player.Equipment = pickle.load(f)

    if os.path.isfile(inventory_file_path):
        if os.stat(inventory_file_path).st_size != 0:
            with open(inventory_file_path, 'rb') as f:
                Player.Inventory = pickle.load(f)
