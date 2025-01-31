
rows, cols = [int(x) for x in input().split(',')]
matrix = []
pos = [0, 0]
cheese_remaining = 0
is_game_ongoing = True

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}


for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'M':
            pos = [row, col]
        elif matrix[row][col] == 'C':
            cheese_remaining += 1

matrix[pos[0]][pos[1]] = '*'

while is_game_ongoing:
    command = input()
    if command == 'danger':
        if cheese_remaining > 0:
            print("Mouse will come back later!")
            break
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]
    if not(0 <= dest_row < rows and 0<= dest_col < cols):
        print("No more cheese for tonight!")
        break
    if matrix[dest_row][dest_col] == '@':
        continue
    pos = [dest_row, dest_col]
    if matrix[dest_row][dest_col] == 'C':
        matrix[dest_row][dest_col] = "*"
        cheese_remaining -= 1
        if cheese_remaining == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[dest_row][dest_col] == 'T':
        print("Mouse is trapped!")
        break

matrix[pos[0]][pos[1]] = 'M'

[print(*row, sep='') for row in matrix]
