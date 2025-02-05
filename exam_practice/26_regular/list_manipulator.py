def list_manipulator(list_of_number, *args):
    output = list(list_of_number)
    command = args[0]
    parameter = args[1]
    values = args[2:]
    if command == 'add':
        if parameter == 'beginning':
            values = reversed(values)
            for v in values:
                output.insert(0, v)
        elif parameter == 'end':
            for v in values:
                output.append(v)
    elif command == 'remove':
        if parameter == 'beginning':
            if values:
                for _ in range(values[0]):
                    output.pop(0)
            else:
                output.pop(0)
        elif parameter == 'end':
            if values:
                for _ in range(values[0]):
                    output.pop()
            else:
                output.pop()
    return output

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))