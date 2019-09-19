from Classes import Player
from Checks import CheckHealing

def Death():
    '''Revives the player when there is no other way to gain hp'''

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

def DeathCheck():
    '''Checks if the player has no other options to heal'''

    if Player.gold <= 0 and CheckHealing() == False:
        Death()
