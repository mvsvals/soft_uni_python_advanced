def numbers_searching(*args):
    my_list = list(args)
    output = [0, []]
    for i in range(min(args), max(args) + 1):
        if i in my_list:
            if my_list.count(i) > 1:
                output[1].append(i)
        else:
            output[0] = i
    output[1].sort()
    return output


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))