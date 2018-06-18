from Classes import QuestInfo
from Classes import Directions
from Classes import Features
from Classes import Player
from Battle import QuestFight
from Drops import QuestReward
from InventoryAndItems import Items
from InventoryAndItems import InvenInsert

def Quests():

    def KillTheRats():
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
        if QuestInfo.QuestNumber == 2:
            if QuestInfo.QuestSeen == False:
                print("QUEST NAME: Find The Castle\n")
                print("You are finally ready for a much grander quest.")
                print("Search for a Castle hidden in the forest.")
                print("You will have to go up, down, left, right and all around.")
                QuestInfo.QuestSeen = True

            CastleLocation = [Directions.UP.value, Directions.UP.value, Directions.RIGHT.value, Directions.UP.value, Directions.LEFT.value]

            print(CastleLocation)
            print("\n")
            print(Features.LastDirections)

            if Features.LastDirections == CastleLocation:
                print("You have found the castle!!!")
                print("Now you must battle all the way to the top\n")

                print("The first opponent is a Guard of the castle")
                QuestFight("Guard",20,10,8,5,200)

                if QuestInfo.Win == True:
                    print("You have made it into the castle")
                    print("Now you have to fight a Knight")
                    QuestFight("Knight",50,25,20,15,575)

                if QuestInfo.Win == True:
                    print("You have passed the Knight")
                    print("Know you must fight the King to take the castle")
                    QuestFight("King",100,50,50,20,1000)

                # TODO: Figure out why the Kings drop gets dublicated when equiped
                if QuestInfo.Win == True:
                    print("Congragulations on captureing the caslte and completing the quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestInfo.QuestSeen = False
                    QuestReward()
                    if Player.Pclass == 'swordsman':
                        Items['Kings Sword'] = list((60,0,120,'weapon','swordsman',0,0,0))
                        InvenInsert('Kings Sword')
                        print("You were also given a Kings Sword!")
                    elif Player.Pclass == 'wizard':
                        Items['Kings Staff'] = list((70,0,200,'weapon','wizard',0,0,0))
                        InvenInsert('Kings Staff')
                        print("You were also given a Kings Staff")
                    elif Player.Pclass == 'rouge':
                        Items['Kings Dagger'] = list((55,0,100,'weapon','rouge',0,0,0))
                        InvenInsert('Kings Dagger')
                        print("You were also given a Kings Dagger")
                    else:
                        print("Could not give out reward")
        QuestInfo.Win = True
    FindTheCastle()
