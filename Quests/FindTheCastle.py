from Classes import QuestInfo
from Classes import Directions
from Classes import Player
from Classes import Features
from Classes import enemy
from Battle import battle
from Drops import QuestReward
from Items import Items
from Inventory import InvenInsert
from helperUtilities import pause

def FindTheCastle():
    '''Quest for finding and conquring a castle'''

    if QuestInfo.QuestNumber == 2:
        if QuestInfo.QuestSeen == False:
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
            battle(enemy("Guard",20,10,8,200,5,20,True))

            if QuestInfo.Win == True:
                print("You have made it into the castle")
                print("Now you have to fight a Knight")
                pause()
                battle(enemy("Knight",50,25,20,575,15,50,True))

            if QuestInfo.Win == True:
                print("You have passed the Knight")
                print("Know you must fight the King to take the castle")
                pause()
                battle(enemy("King",100,50,50,1000,20,100,True))

            # TODO: Figure out why the Kings drop gets dublicated when equiped
            if QuestInfo.Win == True:
                print("Congragulations on captureing the caslte and completing the quest\n")
                QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                QuestInfo.QuestSeen = False
                QuestInfo.InQuest = True
                QuestReward()
                if Player.Pclass == 'swordsman':
                    reward = QuestWeaponAndArmor(
                        'Kings Sword',list((35,0,120,'weapon','swordsman',0,0,0)),
                        'Kings Armor',list((35,0,120,'weapon','swordsman',0,0,0)))
                    CastleQuestReward(reward)
                elif Player.Pclass == 'wizard':
                    reward = QuestWeaponAndArmor(
                        'Kings Staff',list((40,0,200,'weapon','wizard',0,0,0)),
                        'Kings Cloth',list((0,15,100,'armor','wizard',150,0,0)))
                    CastleQuestReward(reward)
                elif Player.Pclass == 'rouge':
                    reward = QuestWeaponAndArmor(
                        'Kings Staff',list((30,0,100,'weapon','rouge',0,0,0)),
                        'Kings Cloth',list((0,20,100,'armor','rouge',60,0,0)))
                    CastleQuestReward(reward)
                else:
                    print("Could not give out reward")
    QuestInfo.Win = True

def CastleQuestReward(reward):
    '''Assigns quest reward to player'''

    Items[reward.weaponName] = reward.weaponStats
    Items[reward.armorName] = reward.armorStats
    InvenInsert(reward.weaponName)
    InvenInsert(reward.armorName)
    print("You were also given a " + reward.weaponName + " & " + reward.armorName)
    pause()

class QuestWeaponAndArmor():
    '''QuestWeaponAndArmor Class'''
    weaponName = ''
    weaponStats = []
    armorName = ''
    armorStats = []
