from Battle.Monsters import MonsterList
from Classes.Classes import *
from Battle.Levels import LevelUp
from Battle.Drops import MonsterDrop
from Battle.Death import Death
from Utilities.HelperUtilities import enum
from Utilities.HelperUtilities import Print
import random

EnemyOrPlayer = enum('PLAYER', 'ENEMY')
ENEMYSTATS = Enemy()

def _instantiateEnemyStats(Enemy):
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

    return Enemy(
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

    _instantiateEnemyStats(enemy)
    _enemyIntroduction()
    _battleLoop()
    print("")
    _lose()
    _win()
    Death()

def _enemyIntroduction():
    '''Introduction for the start of battle'''

    print("It's a " + ENEMYSTATS.name)

    if ENEMYSTATS.questFight == True:
        QuestInfo.InQuest = True

def _getDamage(enemyOrPlayer):
    '''Gets the damage for the player or enemy'''

    if enemyOrPlayer == EnemyOrPlayer.PLAYER:
        damage = _decideDamageCalc(Player.Strength, ENEMYSTATS.defense, enemyOrPlayer)
    else:
        damage = _decideDamageCalc(ENEMYSTATS.attack, Player.Defense, enemyOrPlayer)

    return 0 if damage < 0 else damage

def _decideDamageCalc(attack, defense, enemyOrPlayer):
    '''Determining how to calculate the damage'''

    randAtk = random.randrange(attack)
    randDfs = random.randrange(defense)

    if enemyOrPlayer == EnemyOrPlayer.PLAYER:
        return randAtk - (randDfs + ENEMYSTATS.lvl)
    else:
        return (randAtk + ENEMYSTATS.lvl) - (randDfs + (Player.lvl * 2))

def _battleLoop():
    '''Main loop for the battle'''

    while Player.hp > 0 and ENEMYSTATS.HP > 0:
        Pdamage = _getDamage(EnemyOrPlayer.PLAYER)
        Edamage = _getDamage(EnemyOrPlayer.ENEMY)

        _playersTurn(Pdamage)

        if ENEMYSTATS.HP <= 0:
            break

        _enemysTurn(Edamage)

def _lose():
    '''Losing state for player'''

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        if ENEMYSTATS.questFight == True:
            QuestInfo.Win = False

def _win():
    '''Winning state for player'''

    if Player.hp > 0:
        Print("YOU WON!!!", 0.3)
        exp = random.randrange(0, ENEMYSTATS.exp) + (ENEMYSTATS.lvl * 2)
        Player.exp += exp
        Print("You gained " + str(exp) + " exp", 0.3)
        LevelUp()
        Print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp), 0.3)
        MonsterDrop(ENEMYSTATS.lvl)

        if ENEMYSTATS.questFight == False:
            if ENEMYSTATS.name in QuestInfo.MonstersKilled:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] += 1
            else:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] = 1

def _playersTurn(Pdamage):
    '''Players turn to attack'''

    Print("You hit the " + ENEMYSTATS.name + " for " + str(Pdamage) + " damage")
    ENEMYSTATS.HP -= Pdamage
    Print(ENEMYSTATS.name + " now has " + str(ENEMYSTATS.HP) + " life left.")

def _enemysTurn(Edamage):
    '''Enemys turn to attack'''

    Print(ENEMYSTATS.name + " hit you for " + str(Edamage) + " damage")
    Player.hp -= Edamage
    Print("You have " + str(Player.hp) + " life left.")
