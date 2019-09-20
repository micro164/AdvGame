from Classes import Player
from Classes import Features
from Classes import QuestInfo
from Battle import fight
from Checks import CheckHealing
from Quests.Quests import Quests
from Forest.forestSurprises import *
from Death import Death
import random

def ForestIntro():
    '''The introduction to entering the forest'''

    if Player.hp > 0:
        print("Welcome to the forest!")
    elif Player.hp <= 0:
        if Player.gold <= 0 and CheckHealing() == False:
            Death()
        else:
            print("You do not have enough hp to fight.")
    else:
        print("ERROR: Can't Access forest")

def forest():
    '''The menu for exploring the forest'''

    ForestIntro()
    choice = " "
    random.seed()

    while choice != "5" and Player.hp != 0:
        print("1.up \n2.left \n3.right \n4.down \n5.exit")
        choice = input()
        print("")

        if choice >= "1" and choice <= "4":
            _movePlayer(choice)
        elif choice == "5":
            print("Leaving forest")
        else:
            print("Wrong choice")

def _movePlayer(choice):
    DublicateItem(choice)
    randomPlace = randomSpot(choice)
    _DirectionsWent(choice)

    if randomPlace == False:
        Quests()

        if QuestInfo.InQuest == False:
            _randomEncounter()
        else:
            QuestInfo.InQuest = False

def _randomEncounter():
    rand = random.randrange(0,2)

    if rand == 0:
        print("A group of trees")
    elif rand == 1:
        print("You encountered a monster")
        fight()
    else:
        print("ERROR")



def _DirectionsWent(choice):
    '''Keeps track of the last 5 directions the player went

    Arguments:
    choice -- The direction the player chooses

    '''

    if len(Features.LastDirections) == 5:
        Features.LastDirections.clear()

    Features.LastDirections.append(choice)
