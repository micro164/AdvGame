from Classes import QuestInfo

def Quests():

    def KillTheRats():
        if QuestInfo.QuestNumber == 0:
            print("QUEST NAME: Kill The Rats\n")
            print("The first quest on this journey is to kill 10 rats\n")

            if 'rat' in QuestInfo.MonstersKilled.keys():
                print("RATS KILLED: " + str(QuestInfo.MonstersKilled['rat']) + "\n")
                if QuestInfo.MonstersKilled['rat'] >= 10:
                    print("Congragulations you have completed the first quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestReward()
    KillTheRats()

    def GoblinExtermination():
        if QuestInfo.QuestNumber == 1:
            print("QUEST NAME: Goblin Extermination\n")
            print("Kill 10 goblins to complete the quest\n")

            if 'goblin' in QuestInfo.MonstersKilled.keys():
                print("GOBLINS KILLED: " + str(QuestInfo.MonstersKilled['goblin']) + "\n")
                if QuestInfo.MonstersKilled['goblin'] >= 10:
                    print("Congragulations on completing the quest\n")
                    QuestInfo.QuestNumber = QuestInfo.QuestNumber + 1
                    QuestReward()
    GoblinExtermination()
