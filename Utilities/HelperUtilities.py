from time import sleep
import sys

def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)

def pause():
    print("Press enter key to continue...")
    input()

def Print(text, time=None):
    print(text)

    if time is not None:
        sleep(time)
    else:
        sleep(0.5)

def PrintSlow(text, time=None):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        if time is not None:
            sleep(time)
        else:
            sleep(0.1)
    print("")
