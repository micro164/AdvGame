from time import sleep
import sys
from Classes.Classes import Player


def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)


def pause():
    print("Press enter key to continue...")
    input()


def print_text(text, time=None):
    print(text)

    if time is not None:
        sleep(time)
    else:
        sleep(0.5)


def print_slow(text, time=None):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        if time is not None:
            sleep(time)
        else:
            sleep(0.1)
    print("")


def filter_out_self(list_of_players):
    for player in list_of_players:
        if player.uniqueId == Player.uniqueId:
            list_of_players.remove(player)

    return list_of_players
