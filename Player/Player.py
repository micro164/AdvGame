from Classes.Classes import Player
from Player.Equipment import PrintEquip
from Player.Equipment import EquipEquipment
from Player.Inventory import PrintInven
from Items.Items import UseItem
from Utilities.HelperUtilities import PrintSlow
from Utilities.HelperUtilities import Print

def PlayerStats():
    '''Displays the players stats'''

    PrintSlow("Name: " + Player.name)
    PrintSlow("Level: " + str(Player.lvl))
    PrintSlow("HP: " + str(Player.hp) + "/" + str(Player.MaxHP))
    PrintSlow("EXP: " + str(Player.exp) + "/" + str(Player.MaxExp))
    PrintSlow("Strength: " + str(Player.Strength))
    PrintSlow("Defense: " + str(Player.Defense))
    PrintSlow("Gold: " + str(Player.gold))

    PrintSlow("\nEquipment:")
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
