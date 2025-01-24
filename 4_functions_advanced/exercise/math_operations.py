
def math_operations(*args, **kwargs):
    track_index = 1
    for num in args:
        if track_index == 1:
            kwargs['a'] += num
        elif track_index == 2:
            kwargs['s'] -= num
        elif track_index == 3:
            if num == 0:
                track_index += 1
                continue
            kwargs['d'] /= num
        elif track_index == 4:
            kwargs['m'] *= num
        track_index += 1
        if track_index == 5:
            track_index = 1

    return '\n'.join(f'{x[0]}: {x[1]:.1f}' for x in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,

d=33, m=15))