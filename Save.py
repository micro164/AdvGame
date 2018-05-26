from Classes import Player
import _pickle as pickle

def Exit():
    with open('PlayerFile.txt', 'w') as f:
        write_data = f.write(Player.name + "\n")
        write_data = f.write(str(Player.MaxHP) + "\n")
        write_data = f.write(str(Player.hp) + "\n")
        write_data = f.write(str(Player.Strength) + "\n")
        write_data = f.write(str(Player.Defense) + "\n")
        write_data = f.write(str(Player.gold) + "\n")
        write_data = f.write(str(Player.MaxExp) + "\n")
        write_data = f.write(str(Player.exp) + "\n")
        write_data = f.write(str(Player.lvl) + "\n")
        write_data = f.write(Player.Pclass + "\n")

    with open('Equipment.txt','wb') as f:
        pickle.dump(Player.Equipment, f)

    with open('Inventory.txt','wb') as f:
        pickle.dump(Player.Inventory, f)

    return True
