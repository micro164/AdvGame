from Classes.Classes import *
from Battle.Battle import battle
from Battle.Drops import quest_reward
from Items.Items import Items
from Player.Inventory import inventory_insert
from Utilities.HelperUtilities import pause


def find_the_castle():
    """Quest for finding and conquring a castle"""

    if QuestInfo.QuestNumber == 2:
        if not QuestInfo.QuestSeen:
            print("QUEST NAME: Find The Castle\n")
            print("You are finally ready for a much grander quest.")
            print("Search for a Castle hidden in the forest.")
            print("You will have to go up, down, left, right and all around.")
            QuestInfo.QuestSeen = True
            QuestInfo.InQuest = True
            pause()

        CastleLocation = [Directions.UP.value, Directions.UP.value, Directions.RIGHT.value, Directions.UP.value, Directions.LEFT.value]

        if Features.LastDirections == CastleLocation:
            print("You have found the castle!!!")
            print("Now you must battle all the way to the top\n")

            print("The first opponent is a Guard of the castle")
            pause()
            battle(Enemy("Guard", 20, 10, 8, 200, 5, 20, True))

            if QuestInfo.Win:
                print("You have made it into the castle")
                print("Now you have to fight a Knight")
                pause()
                battle(Enemy("Knight", 50, 25, 20, 575, 15, 50, True))

            if QuestInfo.Win:
                print("You have passed the Knight")
                print("Know you must fight the King to take the castle")
                pause()
                battle(Enemy("King", 100, 50, 50, 1000, 20, 100, True))

            # TODO: Figure out why the Kings drop gets dublicated when equiped
            if QuestInfo.Win:
                print("Congragulations on captureing the caslte and completing the quest\n")
                QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                QuestInfo.QuestSeen = False
                QuestInfo.InQuest = True
                quest_reward()
                if Player.Pclass == 'swordsman':
                    reward = QuestWeaponAndArmor()
                    castle_quest_reward(reward)
                elif Player.Pclass == 'wizard':
                    reward = QuestWeaponAndArmor()
                    castle_quest_reward(reward)
                elif Player.Pclass == 'rouge':
                    reward = QuestWeaponAndArmor()
                    castle_quest_reward(reward)
                else:
                    print("Could not give out reward")
    QuestInfo.Win = True


def castle_quest_reward(reward):
    """Assigns quest reward to player"""

    Items[reward.weaponName] = reward.weaponStats
    Items[reward.armorName] = reward.armorStats
    inventory_insert(reward.weaponName)
    inventory_insert(reward.armorName)
    print("You were also given a " + reward.weaponName + " & " + reward.armorName)
    pause()


class QuestWeaponAndArmor:
    """QuestWeaponAndArmor Class"""
    weaponName = ''
    weaponStats = []
    armorName = ''
    armorStats = []
