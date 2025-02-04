
matrix = [input().split() for x in range(6)]
pos_input = input().split(', ')

pos = [int(pos_input[0][1:]), int(pos_input[1][:-1])]# ({row}, {column})


movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break
    direction = command[1]
    dest_row = pos[0] + movement_mapper[direction][0]
    dest_col = pos[1] + movement_mapper[direction][1]
    if command[0] == 'Create':
        value = command[2]
        if matrix[dest_row][dest_col] == '.':
            matrix[dest_row][dest_col] = value
    elif command[0] == 'Update':
        value = command[2]
        if matrix[dest_row][dest_col].isalnum():
            matrix[dest_row][dest_col] = value

    elif command[0] == 'Delete':
        if matrix[dest_row][dest_col].isalnum():
            matrix[dest_row][dest_col] = '.'
    elif command[0] == 'Read':
        if matrix[dest_row][dest_col].isalnum():
            print(matrix[dest_row][dest_col])
    pos = [dest_row, dest_col]

[print(*row) for row in matrix]
