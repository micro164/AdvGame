def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)
