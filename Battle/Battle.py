from Battle.Monsters import monster_list
from Classes.Classes import *
from Battle.Levels import level_up
from Battle.Drops import monster_drop
from Battle.Death import death
from Utilities.HelperUtilities import enum
from Utilities.HelperUtilities import Print
import random

EnemyOrPlayer = enum('PLAYER', 'ENEMY')
ENEMYSTATS = Enemy()


def _instantiate_enemy_stats(enemy):
    """Initialize Enemy Stats"""

    ENEMYSTATS.name = enemy.name
    ENEMYSTATS.HP = enemy.HP
    ENEMYSTATS.attack = enemy.attack
    ENEMYSTATS.defense = enemy.defense
    ENEMYSTATS.exp = enemy.exp
    ENEMYSTATS.lvl = enemy.lvl
    ENEMYSTATS.MaxHP = enemy.MaxHP
    ENEMYSTATS.questFight = enemy.questFight


def fight():
    """Random battles in forest for player"""

    battle(build_enemy())


def build_enemy():
    temp = monster_list()
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
    """Encapsulates battle for forest and quest fight"""

    _instantiate_enemy_stats(enemy)
    _enemy_introduction()
    _battle_loop()
    print("")
    _lose()
    _win()
    death()


def _enemy_introduction():
    """Introduction for the start of battle"""

    print("It's a " + ENEMYSTATS.name)

    if ENEMYSTATS.questFight:
        QuestInfo.InQuest = True


def _get_damage(enemy_or_player):
    """Gets the damage for the player or enemy"""

    if enemy_or_player == EnemyOrPlayer.PLAYER:
        damage = _decide_damage_calculation(Player.Strength, ENEMYSTATS.defense, enemy_or_player)
    else:
        damage = _decide_damage_calculation(ENEMYSTATS.attack, Player.Defense, enemy_or_player)

    return 0 if damage < 0 else damage


def _decide_damage_calculation(attack, defense, enemy_or_player):
    """Determining how to calculate the damage"""

    random_attack = random.randrange(attack)
    random_defense = random.randrange(defense)

    if enemy_or_player == EnemyOrPlayer.PLAYER:
        return random_attack - (random_defense + ENEMYSTATS.lvl)
    else:
        return (random_attack + ENEMYSTATS.lvl) - (random_defense + (Player.lvl * 2))


def _battle_loop():
    """Main loop for the battle"""

    while Player.hp > 0 and ENEMYSTATS.HP > 0:
        Pdamage = _get_damage(EnemyOrPlayer.PLAYER)
        Edamage = _get_damage(EnemyOrPlayer.ENEMY)

        _players_turn(Pdamage)

        if ENEMYSTATS.HP <= 0:
            break

        _enemies_turn(Edamage)


def _lose():
    """Losing state for player"""

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        if ENEMYSTATS.questFight:
            QuestInfo.Win = False


def _win():
    """Winning state for player"""

    if Player.hp > 0:
        Print("YOU WON!!!", 0.3)
        exp = random.randrange(0, ENEMYSTATS.exp) + (ENEMYSTATS.lvl * 2)
        Player.exp += exp
        Print("You gained " + str(exp) + " exp", 0.3)
        level_up()
        Print("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp), 0.3)
        monster_drop(ENEMYSTATS.lvl)

        if not ENEMYSTATS.questFight:
            if ENEMYSTATS.name in QuestInfo.MonstersKilled:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] += 1
            else:
                QuestInfo.MonstersKilled[ENEMYSTATS.name] = 1


def _players_turn(player_damage):
    """Players turn to attack"""

    Print("You hit the " + ENEMYSTATS.name + " for " + str(player_damage) + " damage")
    ENEMYSTATS.HP -= player_damage
    Print(ENEMYSTATS.name + " now has " + str(ENEMYSTATS.HP) + " life left.")


def _enemies_turn(enemy_damage):
    """Enemys turn to attack"""

    Print(ENEMYSTATS.name + " hit you for " + str(enemy_damage) + " damage")
    Player.hp -= enemy_damage
    Print("You have " + str(Player.hp) + " life left.")
