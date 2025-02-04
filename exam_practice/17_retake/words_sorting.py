def words_sorting(*args):
    my_data = {key: sum(ord(x) for x in key) for key in args}
    if sum(my_data.values()) % 2 != 0:
        my_data = sorted(my_data.items(), key=lambda x: -x[1])
    else:
        my_data = sorted(my_data.items(), key=lambda x: x[0])
    return '\n'.join(f'{x[0]} - {x[1]}' for x in my_data)
