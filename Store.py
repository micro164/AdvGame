from InventoryAndItems import Items
from InventoryAndItems import ItemCheck
from InventoryAndItems import PrintInven
from InventoryAndItems import InvenInsert
from Equipment import EquipInsert
from Classes import Item
from Classes import Player
from math import ceil

#The store for the player
def Store():
    print("1.Buy \n2.Sell \n3.Exit")
    choice = input()
    if choice == "1":
        Buy()
    elif choice == "2":
        Sell()
    elif choice == "3":
        print("Thanks for shopping")
    else:
        print("Wrong choice")

#Function for buying store items
def Buy():
    buy = ""

    while buy != '4':
        print("1.Weapon \n2.Armor \n3.Item \n4.Exit")
        buy = input()
        if buy == '1':
            Mbuy('weapon')
        elif buy == '2':
            Mbuy('armor')
        elif buy == '3':
            Mbuy('item')
        elif buy == '4':
            print("\nThank you for shopping with us")
            break;
        else:
            print("\nERROR: could not buy item\n")

#Function for selling store items
def Sell():
    sell = ""
    while sell != "exit":
        PrintInven()
        print("What item do you want to sell from your inventory?")
        print("Type exit to go back")
        sell = input()

        for key, value in list(Player.Inventory.items()):
            if key == sell:
                Igold = ceil((value[Item.price] * .8))
                if value[Item.count] > 1:
                    Player.gold += Igold
                    value[Item.count] -= 1
                    print(value[Item.count])
                    print("\nYou gained " + str(Igold) + " gold.\n")
                elif value[Item.count] == 1:
                    Player.gold += Igold
                    value[Item.count] -= 1
                    print("\nYou gained " + str(Igold) + " gold.\n")
                    del Player.Inventory[sell]
                else:
                    print("ERROR: Can't sell item")

#The main function for buying a weapon, armor, or item
def Mbuy(Stype):
    PrintStore(Stype)
    print("Type the name of the " + Stype + " you want to buy or no to exit")
    item_name = input()
    if item_name == 'no':
        print("\nThank you for shopping with us\n")
    elif item_name != 'no':
        price = 0
        ItemType = ''

        if ItemCheck(item_name) == True:
            price = Items[item_name][Item.price]
            ItemType = Items[item_name][Item.Type]

        if price != 0 and ItemType != '':
            if Player.gold >= price:
                Player.gold -= price
                if ItemType != 'item':
                    print("Do you want to equip the " + item_name + ": yes/no")
                    choice = input()
                    if choice == 'yes':
                        EquipInsert(item_name)
                        if Items[item_name][Item.lvl] > Player.lvl:
                            InvenInsert(item_name)
                            print("The item has been put in your inventory")
                    elif choice == 'no':
                        InvenInsert(item_name)
                    else:
                        print("ERROR: Could not put away or equip " + item_name)
                elif ItemType == 'item':
                    print("Item put in your inventory.")
                    InvenInsert(item_name)
                else:
                    print("ERROR: Something went wrong with buying item")
            else:
                print("\nYou do not have enough money\n")

        elif price == 0 and ItemType != '':
            print("Unidentified item")
        else:
            print("ERROR: can't buy item")

#Printing out store items
def PrintStore(Stype):
    for key, value in list(Items.items()):
        if (value[Item.Pclass] == Player.Pclass or  value[Item.Type] == 'item') and (value[Item.Type] == Stype):
            if value[Item.lvl] >= Player.lvl and value[Item.lvl] <= (Player.lvl + 5):
                print(key + ": " + str(value[Item.price]))
