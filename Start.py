import os
from Classes import Player
import _pickle as pickle

def Start():

    if os.stat('PlayerFile.txt').st_size != 0:

        with open('PlayerFile.txt') as f:
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

    if os.stat("Equipment.txt").st_size != 0:
        with open('Equipment.txt', 'rb') as f:
            Player.Equipment = pickle.load(f)

    if os.stat("Inventory.txt").st_size != 0:
        with open('Inventory.txt', 'rb') as f:
            Player.Inventory = pickle.load(f)
