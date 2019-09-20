def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)

def pause():
    print("Press enter key to continue...")
    input()
