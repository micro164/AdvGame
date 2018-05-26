from Monsters import MonsterList
import random
from Classes import Player
from Classes import Monster
from Levels import LevelUp
from Drops import MonsterDrop
from Death import Death

#Player encounters a random monster
def fight():
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

    Death()
