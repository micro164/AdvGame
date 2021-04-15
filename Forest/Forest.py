from Classes.Classes import *
from Battle.Battle import fight
from Utilities.Checks import check_healing
from Quests.Quests import Quests
from Forest.ForestSurprises import *
from Battle.Death import death
from Utilities.HelperUtilities import print_text
from Utilities.HelperUtilities import print_slow
from time import sleep
import random


def forest_intro():
	'''The introduction to entering the forest'''

	if Player.hp > 0:
		print_slow("Welcome to the forest!", 0.05)
	elif Player.hp <= 0:
		if Player.gold <= 0 and check_healing() == False:
			death()
		else:
			print("You do not have enough hp to fight.")
	else:
		print("ERROR: Can't Access forest")


def forest():
	'''The menu for exploring the forest'''

	forest_intro()
	choice = " "
	random.seed()

	while choice != "5" and Player.hp != 0:
		sleep(0.5)
		print("1.up \n2.left \n3.right \n4.down \n5.exit")
		choice = input()
		print("")

		if choice >= "1" and choice <= "4":
			_move_player(choice)
		elif choice == "5":
			print("Leaving forest")
		else:
			print("Wrong choice")


def _move_player(choice):
	duplicate_item(choice)
	randomPlace = random_spot(choice)
	_directions_went(choice)

	if randomPlace == False:
		Quests()

		if QuestInfo.InQuest == False:
			_random_encounter()
		else:
			QuestInfo.InQuest = False


def _random_encounter():
	rand = random.randrange(0, 2)

	if rand == 0:
		print("A group of trees\n")
	elif rand == 1:
		print_text("You encountered a monster")
		fight()
	else:
		print("ERROR")


def _directions_went(choice):
	'''Keeps track of the last 5 directions the player went

	Arguments:
	choice -- The direction the player chooses

	'''

	if len(Features.LastDirections) == 5:
		Features.LastDirections.clear()

	Features.LastDirections.append(choice)
