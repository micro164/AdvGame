from Classes import QuestInfo
from Drops import QuestReward
from helperUtilities import pause

def KillTheRats():
    '''Quest to kill 10 rats'''

    if QuestInfo.QuestNumber == 0:
        if QuestInfo.QuestSeen == False:
            print("QUEST NAME: Kill The Rats\n")
            print("The first quest on this journey is to kill 10 rats\n")
            QuestInfo.QuestSeen = True
            QuestInfo.InQuest = True
            pause()

        if 'rat' in QuestInfo.MonstersKilled.keys():
            print("RATS KILLED: " + str(QuestInfo.MonstersKilled['rat']) + "\n")
            if QuestInfo.MonstersKilled['rat'] >= 10:
                print("Congragulations you have completed the first quest\n")
                QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                QuestInfo.QuestSeen = False
                QuestInfo.InQuest = True
                QuestReward()
                pause()

def GoblinExtermination():
    '''Quest to kill 10 goblins'''

    if QuestInfo.QuestNumber == 1:
        if QuestInfo.QuestSeen == False:
            print("QUEST NAME: Goblin Extermination\n")
            print("Kill 10 goblins to complete the quest\n")
            QuestInfo.QuestSeen = True
            QuestInfo.InQuest = True
            pause()

        if 'goblin' in QuestInfo.MonstersKilled.keys():
            print("GOBLINS KILLED: " + str(QuestInfo.MonstersKilled['goblin']) + "\n")
            if QuestInfo.MonstersKilled['goblin'] >= 10:
                print("Congragulations on completing the quest\n")
                QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                QuestInfo.QuestSeen = False
                QuestInfo.InQuest = True
                QuestReward()
                pause()
