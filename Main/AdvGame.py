#!/usr/bin/python3

#Author: Jonathon T. Bryant
#This is a simple text based game created in the language of python
import sys
sys.path.insert(1, '../')

from Items.Items import ItemStats
from Player.Player import DisplayPlayerInventory
from Player.Player import PlayerStats
from Battle.Death import DeathCheck
from Main.Start import Start
from Forest.Forest import forest
from Healing.Healing import Healer
from Store.Store import Store
from Quit.Save import Exit
from Main.GameIntro import GameIntro
from Utilities.HelperUtilities import PrintSlow

def Choices():
    '''Gives the player all the choices for the game'''

    stop = False;
    while stop == False:
        DeathCheck()
        print("\n1.Forest \n2.Healer \n3.Player Stats \n4.Inventory")
        print("5.Item Stats \n6.Store \n7.Exit")
        choice = input()
        print("")
        if choice == "1":
            forest()
        elif choice == "2":
            Healer()
        elif choice == "3":
            PlayerStats()
        elif choice == "4":
            DisplayPlayerInventory()
        elif choice == "5":
            ItemStats()
        elif choice == "6":
            Store()
        elif choice == "7":
            stop = Exit()
        else:
            print("Wrong Choice")

def main():
    '''Main Game Function'''
    Start()
    GameIntro()
    Choices()

if __name__ == '__main__':
    main()
