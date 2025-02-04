def flights(*args):
    output = {}
    for i in range(0, len(args), 2):
        if args[i] == 'Finish':
            return output
        else:
            destination, passengers = args[i], int(args[i + 1])
            if destination not in output:
                output[destination] = 0
            output[destination] += passengers

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))