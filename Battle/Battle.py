from Battle.Monsters import monster_list
from Classes.Classes import *
from Battle.Levels import level_up
from Battle.Drops import monster_drop
from Battle.Death import death
from Utilities.HelperUtilities import enum, print_slow
from Utilities.HelperUtilities import print_text
import random

EnemyOrPlayer = enum('PLAYER', 'ENEMY')
ENEMY_STATS = Enemy()


def _instantiate_enemy_stats(enemy):
    """Initialize Enemy Stats"""

    ENEMY_STATS.name = enemy.name
    ENEMY_STATS.HP = enemy.HP
    ENEMY_STATS.attack = enemy.attack
    ENEMY_STATS.defense = enemy.defense
    ENEMY_STATS.exp = enemy.exp
    ENEMY_STATS.lvl = enemy.lvl
    ENEMY_STATS.MaxHP = enemy.MaxHP
    ENEMY_STATS.questFight = enemy.questFight


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
    print("")
    _battle_loop()
    print("")
    _lose()
    _win()
    death()


def _enemy_introduction():
    """Introduction for the start of battle"""

    print_slow("It's a " + ENEMY_STATS.name, 0.05)

    if ENEMY_STATS.questFight:
        QuestInfo.InQuest = True


def _get_damage(enemy_or_player):
    """Gets the damage for the player or enemy"""

    if enemy_or_player == EnemyOrPlayer.PLAYER:
        damage = _decide_damage_calculation(Player.Strength, ENEMY_STATS.defense, enemy_or_player)
    else:
        damage = _decide_damage_calculation(ENEMY_STATS.attack, Player.Defense, enemy_or_player)

    return 0 if damage < 0 else damage


def _decide_damage_calculation(attack, defense, enemy_or_player):
    """Determining how to calculate the damage"""

    random_attack = random.randrange(attack)
    random_defense = random.randrange(defense)

    if enemy_or_player == EnemyOrPlayer.PLAYER:
        return random_attack - (random_defense + ENEMY_STATS.lvl)
    else:
        return (random_attack + ENEMY_STATS.lvl) - (random_defense + (Player.lvl * 2))


def _battle_loop():
    """Main loop for the battle"""

    while Player.hp > 0 and ENEMY_STATS.HP > 0:
        player_damage = _get_damage(EnemyOrPlayer.PLAYER)
        enemy_damage = _get_damage(EnemyOrPlayer.ENEMY)

        _players_turn(player_damage)
        print("")

        if ENEMY_STATS.HP <= 0:
            break

        _enemies_turn(enemy_damage)
        print("")


def _lose():
    """Losing state for player"""

    if Player.hp <= 0:
        Player.hp = 0
        print("YOU LOSE!!")
        if ENEMY_STATS.questFight:
            QuestInfo.Win = False


def _win():
    """Winning state for player"""

    if Player.hp > 0:
        print_slow("YOU WON!!!", 0.05)
        exp = random.randrange(0, ENEMY_STATS.exp) + (ENEMY_STATS.lvl * 2)
        Player.exp += exp
        print_slow("You gained " + str(exp) + " exp", 0.05)
        level_up()
        print_slow("EXP: " + str(Player.MaxExp) + "/" + str(Player.exp), 0.05)
        monster_drop(ENEMY_STATS.lvl)

        if not ENEMY_STATS.questFight:
            if ENEMY_STATS.name in QuestInfo.MonstersKilled:
                QuestInfo.MonstersKilled[ENEMY_STATS.name] += 1
            else:
                QuestInfo.MonstersKilled[ENEMY_STATS.name] = 1


def _players_turn(player_damage):
    """Players turn to attack"""

    print_slow("You hit the " + ENEMY_STATS.name + " for " + str(player_damage) + " damage", 0.05)
    ENEMY_STATS.HP -= player_damage
    print_slow(ENEMY_STATS.name + " now has " + str(ENEMY_STATS.HP) + " life left.", 0.05)


def _enemies_turn(enemy_damage):
    """Enemies turn to attack"""

    print_slow(ENEMY_STATS.name + " hit you for " + str(enemy_damage) + " damage", 0.05)
    Player.hp -= enemy_damage
    print_slow("You have " + str(Player.hp) + " life left.", 0.05)
