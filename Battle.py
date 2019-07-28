from Monsters import MonsterList
from Classes import Player
from Classes import Monster
from Classes import enemy
from Classes import QuestInfo
from Levels import LevelUp
from Drops import MonsterDrop
from Death import Death
import random

#Player encounters a random monster
def fight():
    '''Random battles in forest for player'''

    temp = MonsterList()
    random.seed()
    key = random.choice(list(temp.items()))
    value = key[1]

    battle(enemy(
        key[0],
        value[Monster.HP],
        value[Monster.attack],
        value[Monster.defense],
        value[Monster.exp],
        value[Monster.lvl],
        value[Monster.MaxHP],
        False
        ))

def battle(Enemy):
    '''Encapsulates battle for forest and quest fight

    Arguments:
    Monster -- Monster class with all of the monsters characteristics

    '''
    print("It's a " + Enemy.name)
    Pdamage = 0
    Edamage = 0

    if Enemy.questFight == True:
        QuestInfo.InQuest = True

    while Player.hp > 0 and Enemy.HP > 0:
        Pdamage = random.randrange(Player.Strength) - (random.randrange(Enemy.defense) + Enemy.lvl)
        Edamage = (random.randrange(Enemy.attack) + Enemy.lvl) - (random.randrange(Player.Defense) + (Player.lvl * 2))

        if Pdamage < 0:
            Pdamage = 0

        if Edamage < 0:
            Edamage = 0


        print("You hit the " + Enemy.name + " for " + str(Pdamage) + " damage")
        Enemy.HP -= Pdamage
        print(Enemy.name + " now has " + str(Enemy.HP) + " life left.")
        if Enemy.HP <= 0:
            break
        print(Enemy.name + " hit you for " + str(Edamage) + " damage")
        Player.hp -= Edamage
        print("You have " + str(Player.hp) + " life left.")

    print("")

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        if Enemy.questFight == True:
            QuestInfo.Win = False

    if Player.hp > 0:
        print("YOU WON!!!")
        exp = random.randrange(0, Enemy.exp) + (Enemy.lvl * 2)
        Player.exp += exp
        print("You gained " + str(exp) + " exp")
        LevelUp()
        print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
        MonsterDrop(Enemy.lvl)

        if Enemy.questFight == False:
            if Enemy.name in QuestInfo.MonstersKilled:
                QuestInfo.MonstersKilled[Enemy.name] += 1
            else:
                QuestInfo.MonstersKilled[Enemy.name] = 1

    Death()
