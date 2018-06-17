from Classes import QuestInfo
from Classes import Directions
from Classes import Features
from Battle import QuestFight
from Drops import QuestReward

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
                QuestFight("Guard",2,10,8,5,20)

                if QuestInfo.Win == True:
                    print("You have made it into the castle")
                    print("Now you have to fight a Knight")
                    QuestFight("Knight",5,25,20,15,75)

                if QuestInfo.Win == True:
                    print("You have passed the Knight")
                    print("Know you must fight the King to take the castle")
                    QuestFight("King",10,50,50,25,1000)

                if QuestInfo.Win == True:
                    print("Congragulations on captureing the caslte and completing the quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestInfo.QuestSeen = False
                    QuestReward()
        QuestInfo.Win = True
    FindTheCastle()
