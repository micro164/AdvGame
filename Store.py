from InventoryAndItems import Items
from InventoryAndItems import ItemCheck
from InventoryAndItems import PrintInven
from InventoryAndItems import InvenInsert
from Equipment import EquipInsert
from Checks import EquipCheck
from Classes import Item
from Classes import Player
from math import ceil

#The store for the player
def Store():
    '''Gives the options for the store'''

    print("1.Buy \n2.Sell \n3.Augmentation \n4.Exit")
    choice = input()
    if choice == "1":
        Buy()
    elif choice == "2":
        Sell()
    elif choice == "3":
        Augmentation()
    elif choice == "4":
        print("Thanks for shopping")
    else:
        print("Wrong choice")

#Function for buying store items
def Buy():
    '''Gives the menu to the player for buying items/weapons/armor'''

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
    '''Menu for player selling an item/armor/weapon'''

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
                    if EquipCheck(key) == False:
                        Player.gold += Igold
                        value[Item.count] -= 1
                        print("\nYou gained " + str(Igold) + " gold.\n")
                        del Player.Inventory[sell]
                    else:
                        print("\nThat item is currently equipped\n")
                else:
                    print("\nERROR: Can't sell item\n")

#The main function for buying a weapon, armor, or item
def Mbuy(Stype):
    '''Gives the menu for player to buy a weapon, armor, or item

    Arguments:
    Stype -- the type of the item that the player is tring to buy

    '''

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

            if Player.gold >= price:
                Player.gold -= price
                if ItemType != 'item':
                    print("Do you want to equip the " + item_name + ": yes/no")
                    choice = input()
                    if choice == 'yes':
                        EquipInsert(item_name)
                        if Items[item_name][Item.lvl] > Player.lvl:
                            InvenInsert(item_name)
                            print("The item has been put in your inventory\n")
                    elif choice == 'no':
                        InvenInsert(item_name)
                    else:
                        print("\nERROR: Could not put away or equip " + item_name + "\n")
                elif ItemType == 'item':
                    print("Item put in your inventory.\n")
                    InvenInsert(item_name)
                else:
                    print("\nERROR: Something went wrong with buying item\n")
            else:
                print("\nYou do not have enough money\n")
        else:
            print("\nERROR: can't buy item\n")

#Printing out store items
def PrintStore(Stype):
    '''Prints all the items in the store for the player

    Arguments:
    Stype -- the type of the item that the player is trying to buy

    '''

    for key, value in list(Items.items()):
        if (value[Item.Pclass] == Player.Pclass or  value[Item.Type] == 'item') and (value[Item.Type] == Stype):
            if value[Item.lvl] >= Player.lvl and value[Item.lvl] <= (Player.lvl + 5):
                print(key + ": " + str(value[Item.price]))

def Augmentation():
    '''Allows the player to augment their weapon or armor'''

    print("\nWelcome to the augmentation center.")
    print("Please select what you want to augment")
    print("\n1.Weapon \n2.Armor")

    choice = input()

    if choice == "1":
        AugmentItem("weapon")
    elif choice == "2":
        AugmentItem("armor")
    else:
        print("wrong key")

def AugmentItem(typeOfItem):
    '''Actual augmentation of weapon or armor

    Arguments:
    typeOfItem -- the type of item that the player is trying to augment

    '''

    for key, value in list(Player.Equipment.items()):
            if value[Item.Type] == typeOfItem:
                cToInt = 0

                for c in value[Item.Pclass]:
                    cToInt = cToInt + ord(c)

                price = value[Item.lvl] * int((cToInt / len(value[Item.Pclass])))

                print("\nThe price to augment the " + typeOfItem + " will be " + str(price) + ".")
                print("Do you accept the charges? (y/n)")

                accept = input()

                if accept == 'y' or accept == 'Y':
                    if Player.gold >= price:
                        Player.gold = Player.gold - price

                        if typeOfItem == 'weapon':
                            Player.Strength = Player.Strength - value[Item.attack]
                            value[Item.attack] = value[Item.attack] + value[Item.lvl]
                            Player.Strength = Player.Strength + value[Item.attack]
                            print("Your weapon now has " + str(value[Item.attack]) + " attack\n")

                        if typeOfItem == 'armor':
                            Player.Defense = Player.Defense - value[Item.defense]
                            value[Item.defense] = value[Item.defense] + value[Item.lvl]
                            Player.Defense = Player.Defense + value[Item.defense]
                            print("Your armor now has " + str(value[Item.defense]) + " defense\n")

                    else:
                        print("Not enough gold.\n")
                elif accept == 'n' or accept == 'N':
                    print("Thank you for coming\n")
                else:
                    print("ERROR: wrong key pressed")
