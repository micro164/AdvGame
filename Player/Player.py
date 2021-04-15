from Classes.Classes import Player
from Player.Equipment import print_equip
from Player.Equipment import equip_equipment
from Player.Inventory import print_inventory
from Items.Items import use_item
from Utilities.HelperUtilities import print_slow
from Utilities.HelperUtilities import print_text

def PlayerStats():
    '''Displays the players stats'''

    print_slow("Name: " + Player.name)
    print_slow("Level: " + str(Player.lvl))
    print_slow("HP: " + str(Player.hp) + "/" + str(Player.MaxHP))
    print_slow("EXP: " + str(Player.exp) + "/" + str(Player.MaxExp))
    print_slow("Strength: " + str(Player.Strength))
    print_slow("Defense: " + str(Player.Defense))
    print_slow("Gold: " + str(Player.gold))

    print_slow("\nEquipment:")
    print_equip()

def DisplayPlayerInventory():
    '''Displays the players inventory'''

    choice = ''
    while choice != '4':
        print_inventory()

        print_text("\n1. Equip a weapon or armor")
        print_text("2. Use an item")
        print_text("3. Exit")

        choice = input()

        if choice == '1':
            equip_equipment()
        elif choice == '2':
            use_item()
        elif choice == '3':
            print("Exiting inventory")
            choice = '4'
