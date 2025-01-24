def even_odd_filter(**kwargs):
    output = {}
    for key, value in kwargs.items():
        if key == 'odd':
            output[key] = [num for num in value if int(num) % 2 != 0]
        elif key == 'even':
            output[key] = [num for num in value if int(num) % 2 == 0]
    return dict(sorted(output.items(), key= lambda x: -len(x[1])))

