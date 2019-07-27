from Classes import QuestInfo
from Classes import Directions
from Classes import Features
from Classes import Player
from Classes import enemy
from Battle import battle
from Drops import QuestReward
from InventoryAndItems import Items
from InventoryAndItems import InvenInsert

def Quests():
    '''Function where all of the players quests reside'''

    def KillTheRats():
        '''Quest to kill 10 rats'''

        if QuestInfo.QuestNumber == 0:
            if QuestInfo.QuestSeen == False:
                print("QUEST NAME: Kill The Rats\n")
                print("The first quest on this journey is to kill 10 rats\n")
                QuestInfo.QuestSeen = True

            if 'rat' in QuestInfo.MonstersKilled.keys():
                print("RATS KILLED: " + str(QuestInfo.MonstersKilled['rat']) + "\n")
                if QuestInfo.MonstersKilled['rat'] >= 10:
                    print("Congragulations you have completed the first quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestInfo.QuestSeen = False
                    QuestReward()
    KillTheRats()

    def GoblinExtermination():
        '''Quest to kill 10 goblins'''

        if QuestInfo.QuestNumber == 1:
            if QuestInfo.QuestSeen == False:
                print("QUEST NAME: Goblin Extermination\n")
                print("Kill 10 goblins to complete the quest\n")
                QuestInfo.QuestSeen = True

            if 'goblin' in QuestInfo.MonstersKilled.keys():
                print("GOBLINS KILLED: " + str(QuestInfo.MonstersKilled['goblin']) + "\n")
                if QuestInfo.MonstersKilled['goblin'] >= 10:
                    print("Congragulations on completing the quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestInfo.QuestSeen = False
                    QuestReward()
    GoblinExtermination()

    def FindTheCastle():
        '''Quest for finding and conquring a castle'''

        if QuestInfo.QuestNumber == 2:
            if QuestInfo.QuestSeen == False:
                print("QUEST NAME: Find The Castle\n")
                print("You are finally ready for a much grander quest.")
                print("Search for a Castle hidden in the forest.")
                print("You will have to go up, down, left, right and all around.")
                QuestInfo.QuestSeen = True

            CastleLocation = [Directions.UP.value, Directions.UP.value, Directions.RIGHT.value, Directions.UP.value, Directions.LEFT.value]

            if Features.LastDirections == CastleLocation:
                print("You have found the castle!!!")
                print("Now you must battle all the way to the top\n")

                print("The first opponent is a Guard of the castle")
                battle(enemy("Guard",20,10,8,200,5,20,True))

                if QuestInfo.Win == True:
                    print("You have made it into the castle")
                    print("Now you have to fight a Knight")
                    battle(enemy("Knight",50,25,20,575,15,50,True))

                if QuestInfo.Win == True:
                    print("You have passed the Knight")
                    print("Know you must fight the King to take the castle")
                    battle(enemy("King",100,50,50,1000,20,100,True))

                # TODO: Figure out why the Kings drop gets dublicated when equiped
                if QuestInfo.Win == True:
                    print("Congragulations on captureing the caslte and completing the quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestInfo.QuestSeen = False
                    QuestReward()
                    if Player.Pclass == 'swordsman':
                        Items['Kings Sword'] = list((35,0,120,'weapon','swordsman',0,0,0))
                        Items['Kings Armor'] = list((0,25,100,'armor','swordsman',50,0,0))
                        InvenInsert('Kings Sword')
                        InvenInsert('Kings Armor')
                        print("You were also given a Kings Sword & Armor!")
                    elif Player.Pclass == 'wizard':
                        Items['Kings Staff'] = list((40,0,200,'weapon','wizard',0,0,0))
                        Items['Kings Cloth'] = list((0,15,100,'armor','wizard',150,0,0))
                        InvenInsert('Kings Staff')
                        InvenInsert('Kings Cloth')
                        print("You were also given a Kings Staff & Cloth")
                    elif Player.Pclass == 'rouge':
                        Items['Kings Dagger'] = list((30,0,100,'weapon','rouge',0,0,0))
                        Items['Kings Cloak'] = list((0,20,100,'armor','rouge',60,0,0))
                        InvenInsert('Kings Dagger')
                        InvenInsert('Kings Cloak')
                        print("You were also given a Kings Dagger & Cloak")
                    else:
                        print("Could not give out reward")
        QuestInfo.Win = True
    FindTheCastle()
