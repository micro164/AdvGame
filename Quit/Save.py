from Classes.Classes import Player

try:
    import _pickle as pickle
except ImportError:
    print("Can't save without the _pickle import")


def Exit():
    '''Saves the players stats'''

    playerFilePath = '../Player/PlayerFile.txt'
    equipmentFilePath = '../Player/Equipment.txt'
    inventoryFilePath = '../Player/Inventory.txt'

    with open(playerFilePath, 'w') as f:
        f.write(Player.name + "\n")
        f.write(str(Player.MaxHP) + "\n")
        f.write(str(Player.hp) + "\n")
        f.write(str(Player.Strength) + "\n")
        f.write(str(Player.Defense) + "\n")
        f.write(str(Player.gold) + "\n")
        f.write(str(Player.MaxExp) + "\n")
        f.write(str(Player.exp) + "\n")
        f.write(str(Player.lvl) + "\n")
        f.write(Player.Pclass + "\n")

    with open(equipmentFilePath,'wb') as f:
        pickle.dump(Player.Equipment, f)

    with open(inventoryFilePath,'wb') as f:
        pickle.dump(Player.Inventory, f)

    return True
