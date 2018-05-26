from Classes import Player

#Function for healing facility for the game
def Healer():
    print("Welcome to the healer.\nWould you like to heal?")
    choice = input("Y/N\n")
    if Player.hp != Player.MaxHP and choice == 'Y' or choice == 'y':
        if Player.gold <= 0:
            print("You do not have any gold to heal!")
        elif Player.gold > 0:
            while Player.hp != Player.MaxHP and Player.gold > 0:
                Player.hp += 1
                Player.gold -= 1

            print("HP: " + str(Player.MaxHP) + "/" + str(Player.hp))
        else:
            print("ERROR: Can not heal")
    elif choice == 'N' or choice == 'n':
        print("Thank you for visiting")
    else:
        print("Wrong choice")
