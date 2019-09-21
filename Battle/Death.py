from Classes.Classes import Player
from Utilities.Checks import CheckHealing

def Death():
    '''Revives the player when there is no other way to gain hp'''

    if Player.hp == 0 and Player.gold == 0:
        HealingItem = CheckHealing()
        checkHealingOptions(HealingItem)

def DeathCheck():
    '''Checks if the player has no other options to heal'''

    if Player.gold <= 0 and CheckHealing() == False:
        Death()

def checkHealingOptions(HealingItem):
    '''Figures out which healing option the player has'''

    if bool(HealingItem) == False and Player.exp > 0:
        noMoneyHealing()
    elif Player.exp == 0 and bool(HealingItem) == False:
        noMoneyAndExpHealing()

def noMoneyHealing():
    '''Heals the player when they have no money'''

    print("Grim Reaper: 'You have no gold to heal yourself. Muhahaha'")
    print("Grim Reaper: 'I will take some experience from you in order to restore your life.'")
    print("")
    Player.exp -= 10 * Player.lvl
    if Player.exp < 0:
        Player.exp = 0
    Player.hp = Player.MaxHP

def noMoneyAndExpHealing():
    '''Heals the player when they have no money or experience'''

    print("Grim Reaper: 'You have nothing so I will add to your Max Exp. to restore your life.'")
    print("")
    Player.MaxExp += 10 * Player.lvl
    Player.hp = Player.MaxHP
