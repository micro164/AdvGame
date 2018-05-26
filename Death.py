from Classes import Player
from Checks import CheckHealing

#Revives player when there is no way to gain hp
def Death():
    if Player.hp == 0 and Player.gold == 0:
        HealingItem = CheckHealing()
        if bool(HealingItem) == False and Player.exp > 0:
            print("Grim Reaper: 'You have no gold to heal yourself. Muhahaha'")
            print("Grim Reaper: 'I will take some experience from you in order to restore your life.'")
            print("")
            Player.exp -= 10 * Player.lvl
            if Player.exp < 0:
                Player.exp = 0
            Player.hp = Player.MaxHP
        elif Player.exp == 0 and bool(HealingItem) == False:
            print("Grim Reaper: 'You have nothing so I will add to your Max Exp. to restore your life.'")
            print("")
            Player.MaxExp += 10 * Player.lvl
            Player.hp = Player.MaxHP

#Checks to see if player has no option to heal
def DeathCheck():
    if Player.gold <= 0 and CheckHealing() == False:
        Death()
