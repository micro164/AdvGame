from Classes import Player
from Equipment import PrintEquip
from Equipment import EquipEquipment
from InventoryAndItems import PrintInven
from InventoryAndItems import UseItem

#Displays the players stats
def PlayerStats():
    print("Name: " + Player.name)
    print("Level: " + str(Player.lvl))
    print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
    print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
    print("Strength: " + str(Player.Strength))
    print("Defense: " + str(Player.Defense))
    print("Gold: " + str(Player.gold))

    print("\nEquipment:")
    PrintEquip()

#Displays the players inventory and asks if what they want to do with the items
def DisplayPlayerInventory():
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
