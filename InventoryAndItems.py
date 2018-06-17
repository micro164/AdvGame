from Classes import Item
from Classes import Player
from Checks import EquipCheck


#Stats for each item in the game
# 0-attack, 1-defense, 2-price, 3-type, 4-Pclass, 5-HP, 6-count, 7-lvl
Items = {'sword': list((10,0,10,'weapon', 'swordsman', 0,0,1)),
         'bronze sword': list((15,0,15,'weapon','swordsman',0,0,5)),
         'iron sword': list((20,0,20,'weapon','swordsman',0,0,10)),
         'steel sword': list((25,0,25,'weapon','swordsman',0,0,15)),
         'long sword': list((30,0,30,'weapon','swordsman',0,0,20)),
         'broad sword': list((40,0,50,'weapon','swordsman',0,0,25)),
         'damascus sword': list((55,0,100,'weapon','swordsman',0,0,30)),
         'Enchanted long sword': list((70,0,150,'weapon','swordsman',0,0,35)),
         'diamond sword': list((100,0,250,'weapon','swordsman',0,0,40)),
         'great sword': list((120,0,300,'weapon','swordsman',0,0,45)),
         'Death sword': list((180,0,400,'weapon','swordsman',0,0,50)),
         'fire sword': list((250,0,600,'weapon','swordsman',0,0,55)),
         'ice sword': list((275,0,650,'weapon','swordsman',0,0,60)),
         'Elemental sword': list((340,0,800,'weapon','swordsman',0,0,65)),
         'sword of ifrit': list((375,0,1000,'weapon','swordsman',0,0,70)),
         'RA\'s sword': list((400,0,1500,'weapon','swordsman',0,0,75)),
         'sword of swords': list((425,0,1800,'weapon','swordsman',0,0,80)),
         'Excalibur': list((475,0,2500,'weapon','swordsman',0,0,85)),
         'elder sword': list((500,0,3000,'weapon','swordsman',0,0,90)),
         'Enchanted ancient sword': list((550,0,4000,'weapon','swordsman',0,0,95)),
         'Dragon sword': list((600,0,5000,'weapon','swordsman',0,0,100)),
         'wand': list((5,0,2,'weapon','wizard',0,0,1)),
         'dagger': list((7,0,5,'weapon','rouge',0,0,1)),
         'bronze armor': list((0,10,10,'armor','swordsman',0,0,1)),
         'cloth armor': list((0,5,2,'armor','wizard',5,0,1)),
         'hard cloth armor': list((0,7,5,'armor','rouge',0,0,1)),
         'potion': list((0,0,20,'item','healer', 20,0,1)),
         'Hyper Potion': list((0,0,50,'item','healer',50,0,20))}

#List of items that monsters drop
def ItemList(Stype):
    temp = {}
    for key, value in list(Items.items()):
        if value[Item.Type] == Stype:
            if value[Item.lvl] <= (Player.lvl + 5):
                temp[key] = Items[key]
    return temp

#Asks user which item they want to use and then applies the appropriate stats
def UseItem():
    print("Enter the name of the item to use")
    item_name = input()
    CheckItem = InvenCheck(item_name)
    if bool(CheckItem) == True:
        for key, value in list(Player.Inventory.items()):
            if key == item_name and value[Item.Type] == "item":
                Player.Strength += value[Item.attack]
                print("\n+" + str(value[Item.attack]) + " attack")
                Player.Defense += value[Item.defense]
                print("+" + str(value[Item.defense]) + " defense")
                if Player.hp < Player.MaxHP:
                    Player.hp += value[Item.HP]
                    print("+" + str(value[Item.HP]) + " HP\n")
                if Player.hp > Player.MaxHP:
                    Player.hp = Player.MaxHP

                print("Strength: " + str(Player.Strength))
                print("Defense: " + str(Player.Defense))
                print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp) + "\n")

                if value[Item.count] > 1:
                    value[Item.count] -= 1
                elif value[Item.count] == 1:
                    value[Item.count] -= 1
                    del Player.Inventory[item_name]
                else:
                    print("ERROR: could not use item")
            elif key == item_name and value[Item.Type] != "item":
                print("\nThis is not an item\n")

#Display a stat of a selected items
def ItemStats():
    item_lookup = ""

    while item_lookup != "exit":
        print("What item do you want to look up?")
        print("Type exit when done")
        item_lookup = input()

        if ItemCheck(item_lookup) == True and item_lookup != "exit":
            print("Name: " + item_lookup)
            print("Attack: " + str(Items[item_lookup][Item.attack]))
            print("Defense: " + str(Items[item_lookup][Item.defense]))
            print("HP: " + str(Items[item_lookup][Item.HP]))
            print("Price: " + str(Items[item_lookup][Item.price]))
            print("Type: " + Items[item_lookup][Item.Type])
            print("Class: " + Items[item_lookup][Item.Pclass] + "\n")
        elif ItemCheck(item_lookup) == False and item_lookup != "exit":
            print("Item not found\n")

#Inserting Item into inventory
def InvenInsert(item_name):
    Player.Inventory[item_name] = Items[item_name]
    Echeck = EquipCheck(item_name)
    if Echeck == False:
        Player.Inventory[item_name][Item.count] += 1

#Prints items in inventory that can be sold
def PrintInven():
    for key, value in list(Player.Inventory.items()):
        print(key + " X " + str(value[Item.count]))

#Checks if item is in player inventory
def InvenCheck(item_name):
    for key, value in list(Player.Inventory.items()):
        if key == item_name:
            return True
    return False

#Checks to see if the name entered is actually an item
def ItemCheck(item_name):
    for key, value in list(Items.items()):
        if key == item_name:
            return True
    return False
