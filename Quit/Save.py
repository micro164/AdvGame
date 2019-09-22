from Classes.Classes import Player

try:
    import _pickle as pickle
except ImportError:
    print("Can't save without the _pickle import")


def exit_and_save():
    '''Saves the players stats'''

    player_file_path = '../Player/PlayerFile.txt'
    equipment_file_path = '../Player/Equipment.txt'
    inventory_file_path = '../Player/Inventory.txt'

    with open(player_file_path, 'w') as f:
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
        f.write(str(Player.uniqueId) + "\n")

    with open(equipment_file_path, 'wb') as f:
        pickle.dump(Player.Equipment, f)

    with open(inventory_file_path, 'wb') as f:
        pickle.dump(Player.Inventory, f)

    return True
