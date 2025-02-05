def best_list_pureness(list_of_numbers, k):
    my_dict = {}
    for rotation in range(k+1):
        pureness  = sum(num * i for i, num in enumerate(list_of_numbers))
        list_of_numbers.insert(0, list_of_numbers.pop())
        if pureness not in my_dict:
            my_dict[pureness] = rotation
    best_pureness = max(my_dict)
    count_rotations = my_dict[best_pureness]
    return f"Best pureness {best_pureness} after {count_rotations} rotations"

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)