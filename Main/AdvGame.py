#!/usr/bin/python3

# Author: Jonathon T. Bryant
# This is a simple text based game created in the language of python

import sys
sys.path.insert(1, '../')

from Items.Items import item_stats
from Player.Player import DisplayPlayerInventory
from Player.Player import PlayerStats
from Battle.Death import death_check
from Main.Start import start
from Forest.Forest import forest
from Healing.Healing import healer
from Store.Store import store
from Quit.Save import exit_and_save
from Main.GameIntro import game_intro


def choices():
    """Gives the player all the choices for the game"""
    stop = False
    while not stop:
        death_check()
        print("\n1.Forest \n2.Healer \n3.Player Stats \n4.Inventory")
        print("5.Item Stats \n6.Store \n7.Exit")
        choice = input()
        print("")
        if choice == "1":
            forest()
        elif choice == "2":
            healer()
        elif choice == "3":
            PlayerStats()
        elif choice == "4":
            DisplayPlayerInventory()
        elif choice == "5":
            item_stats()
        elif choice == "6":
            store()
        elif choice == "7":
            stop = exit_and_save()
        else:
            print("Wrong Choice")


def main():
    """Main Game Function"""
    start()
    game_intro()
    choices()


if __name__ == '__main__':
    main()
