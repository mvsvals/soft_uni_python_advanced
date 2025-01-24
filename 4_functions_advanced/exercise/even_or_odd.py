def even_odd(*args):
    return [x for x in args[:-1] if int(x) % 2 == 0] if args[-1] == 'even' else [x for x in args[:-1] if int(x) % 2 != 0]

