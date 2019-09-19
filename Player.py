from Classes import Player
from Equipment import PrintEquip
from Equipment import EquipEquipment
from InventoryAndItems import PrintInven
from InventoryAndItems import UseItem

def PlayerStats():
    '''Displays the players stats'''

    print("Name: " + Player.name)
    print("Level: " + str(Player.lvl))
    print("HP: " + str(Player.hp) + "/" + str(Player.MaxHP))
    print("EXP: " + str(Player.exp) + "/" + str(Player.MaxExp))
    print("Strength: " + str(Player.Strength))
    print("Defense: " + str(Player.Defense))
    print("Gold: " + str(Player.gold))

    print("\nEquipment:")
    PrintEquip()

def DisplayPlayerInventory():
    '''Displays the players inventory'''

    choice = ''
    while choice != '4':
        PrintInven()

        print("\n1. Equip a weapon or armor")
        print("2. Use an item")
        print("3. Exit")

        choice = input()

        if choice == '1':
            EquipEquipment()
        elif choice == '2':
            UseItem()
        elif choice == '3':
            print("Exiting inventory")
            choice = '4'
