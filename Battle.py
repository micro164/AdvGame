from Monsters import MonsterList
import random
from Classes import Player
from Classes import Monster
from Classes import QuestInfo
from Levels import LevelUp
from Drops import MonsterDrop
from Death import Death

#Player encounters a random monster
def fight():
    '''Random battles in forest for player'''

    temp = MonsterList()
    random.seed()
    key = random.choice(list(temp.items()))
    value = key[1]
    print("It's a " + key[0])
    Pdamage = 0
    Edamage = 0

    while Player.hp > 0 and value[Monster.HP] > 0:
        Pdamage = random.randrange(Player.Strength) - (random.randrange(value[Monster.defense]) + value[Monster.lvl])
        Edamage = (random.randrange(value[Monster.attack]) + value[Monster.lvl]) - (random.randrange(Player.Defense) + (Player.lvl * 2))

        if Pdamage < 0:
            Pdamage = 0

        if Edamage < 0:
            Edamage = 0


        print("You hit the " + key[0] + " for " + str(Pdamage) + " damage")
        value[Monster.HP] -= Pdamage
        print(key[0] + " now has " + str(value[Monster.HP]) + " life left.")
        if value[Monster.HP] <= 0:
            break
        print(key[0] + " hit you for " + str(Edamage) + " damage")
        Player.hp -= Edamage
        print("You have " + str(Player.hp) + " life left.")

    print("")

    if value[Monster.HP] < value[Monster.MaxHP]:
        value[Monster.HP] = value[Monster.MaxHP]

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")

    if Player.hp > 0:
        print("YOU WON!!!")
        exp = random.randrange(0, value[Monster.exp]) + (value[Monster.lvl] * 2)
        Player.exp += exp
        print("You gained " + str(exp) + " exp")
        LevelUp()
        print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
        MonsterDrop(value[Monster.lvl])

        if key[0] in QuestInfo.MonstersKilled:
            QuestInfo.MonstersKilled[key[0]] += 1
        else:
            QuestInfo.MonstersKilled[key[0]] = 1

    Death()

def QuestFight(MonsterName, MonsterHP, MonsterAttack, MonsterDefense, MonsterLvl, MonsterExp):
    '''Quest battles for the player

    Arguments:
    MonsterName -- Name of the monster the player is fighting
    MonsterHP -- The amount of health the monster has
    MonsterAttack -- The amount of attack power the monster has
    MonsterDefense -- The amount of defense power the mosnter has
    MonsterLvl -- The level of the monster
    MonsterExp -- The amount of experence the monster gives

    '''

    print("It's a " + MonsterName)
    Pdamage = 0
    Edamage = 0
    QuestInfo.InQuest = True

    while Player.hp > 0 and MonsterHP > 0:
        Pdamage = random.randrange(Player.Strength) - (random.randrange(MonsterDefense) + MonsterLvl)
        Edamage = (random.randrange(MonsterAttack) + MonsterLvl) - (random.randrange(Player.Defense) + (Player.lvl * 2))

        if Pdamage < 0:
            Pdamage = 0

        if Edamage < 0:
            Edamage = 0


        print("You hit the " + MonsterName + " for " + str(Pdamage) + " damage")
        MonsterHP -= Pdamage
        print(MonsterName + " now has " + str(MonsterHP) + " life left.")
        if MonsterHP <= 0:
            break
        print(MonsterName + " hit you for " + str(Edamage) + " damage")
        Player.hp -= Edamage
        print("You have " + str(Player.hp) + " life left.")

    print("")

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        QuestInfo.Win = False

    if Player.hp > 0:
        print("YOU WON!!!")
        exp = random.randrange(0, MonsterExp) + (MonsterLvl * 2)
        Player.exp += exp
        print("You gained " + str(exp) + " exp")
        LevelUp()
        print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
        MonsterDrop(MonsterLvl)

    Death()
