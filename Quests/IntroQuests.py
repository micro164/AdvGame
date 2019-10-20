from Classes.Classes import QuestInfo
from Battle.Drops import quest_reward
from Utilities.HelperUtilities import pause
from Utilities.HelperUtilities import PrintSlow

def KillTheRats():
    '''Quest to kill 10 rats'''

    if QuestInfo.QuestNumber == 0:
        if QuestInfo.QuestSeen == False:
            PrintSlow("QUEST NAME: Kill The Rats\n")
            PrintSlow("The first quest on this journey is to kill 10 rats\n")
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
                quest_reward()
                pause()

def GoblinExtermination():
    '''Quest to kill 10 goblins'''

    if QuestInfo.QuestNumber == 1:
        if QuestInfo.QuestSeen == False:
            PrintSlow("QUEST NAME: Goblin Extermination\n")
            PrintSlow("Kill 10 goblins to complete the quest\n")
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
                quest_reward()
                pause()
