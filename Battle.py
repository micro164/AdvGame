from Monsters import MonsterList
from Classes import Player
from Classes import Monster
from Classes import enemy
from Classes import QuestInfo
from Levels import LevelUp
from Drops import MonsterDrop
from Death import Death
from helperUtilities import enum
import random

EnemyOrPlayer = enum('PLAYER', 'ENEMY')
ENEMYSTATS = enemy()

def instantiateEnemyStats(Enemy):
    '''Initialize Enemy Stats'''

    ENEMYSTATS.name = Enemy.name
    ENEMYSTATS.HP = Enemy.HP
    ENEMYSTATS.attack = Enemy.attack
    ENEMYSTATS.defense = Enemy.defense
    ENEMYSTATS.exp = Enemy.exp
    ENEMYSTATS.lvl = Enemy.lvl
    ENEMYSTATS.MaxHP = Enemy.MaxHP
    ENEMYSTATS.questFight = Enemy.questFight

def fight():
    '''Random battles in forest for player'''

    battle(buildEnemy())

def buildEnemy():
    temp = MonsterList()
    random.seed()
    key = random.choice(list(temp.items()))
    value = key[1]

    return enemy(
        key[0],
        value[Monster.HP],
        value[Monster.attack],
        value[Monster.defense],
        value[Monster.exp],
        value[Monster.lvl],
        value[Monster.MaxHP],
        False
        )

def battle(enemy):
    '''Encapsulates battle for forest and quest fight'''

    instantiateEnemyStats(enemy)
    enemyIntroduction()
    battleLoop()
    print("")
    lose()
    win()
    Death()

def enemyIntroduction():
    '''Introduction for the start of battle'''

    print("It's a " + ENEMYSTATS.name)

    if ENEMYSTATS.questFight == True:
        QuestInfo.InQuest = True

def getDamage(enemyOrPlayer):
    '''Gets the damage for the player or enemy'''

    if enemyOrPlayer == EnemyOrPlayer.PLAYER:
        damage = decideDamageCalc(Player.Strength, ENEMYSTATS.defense, enemyOrPlayer)
    else:
        damage = decideDamageCalc(ENEMYSTATS.attack, Player.Defense, enemyOrPlayer)

    return 0 if damage < 0 else damage

def decideDamageCalc(attack, defense, enemyOrPlayer):
    '''Determining how to calculate the damage'''

    randAtk = random.randrange(attack)
    randDfs = random.randrange(defense)

    if enemyOrPlayer == EnemyOrPlayer.PLAYER:
        return randAtk - (randDfs + ENEMYSTATS.lvl)
    else:
        return (randAtk + ENEMYSTATS.lvl) - (randDfs + (Player.lvl * 2))

def battleLoop():
    '''Main loop for the battle'''

    while Player.hp > 0 and ENEMYSTATS.HP > 0:
        Pdamage = getDamage(EnemyOrPlayer.PLAYER)
        Edamage = getDamage(EnemyOrPlayer.ENEMY)

        playersTurn(Pdamage)

        if ENEMYSTATS.HP <= 0:
            break

        enemysTurn(Edamage)

def lose():
    '''Losing state for player'''

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        if ENEMYSTATS.questFight == True:
            QuestInfo.Win = False

def win():
    '''Winning state for player'''

    if Player.hp > 0:
        print("YOU WON!!!")
        exp = random.randrange(0, ENEMYSTATS.exp) + (ENEMYSTATS.lvl * 2)
        Player.exp += exp
        print("You gained " + str(exp) + " exp")
        LevelUp()
        print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp))
        MonsterDrop(ENEMYSTATS.lvl)

        if ENEMYSTATS.questFight == False:
            if ENEMYSTATS.name in QuestInfo.MonstersKilled:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] += 1
            else:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] = 1

def playersTurn(Pdamage):
    '''Players turn to attack'''

    print("You hit the " + ENEMYSTATS.name + " for " + str(Pdamage) + " damage")
    ENEMYSTATS.HP -= Pdamage
    print(ENEMYSTATS.name + " now has " + str(ENEMYSTATS.HP) + " life left.")

def enemysTurn(Edamage):
    '''Enemys turn to attack'''

    print(ENEMYSTATS.name + " hit you for " + str(Edamage) + " damage")
    Player.hp -= Edamage
    print("You have " + str(Player.hp) + " life left.")
