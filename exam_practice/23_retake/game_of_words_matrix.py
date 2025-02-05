initial_string = list(input())
size = int(input())

matrix = []
pos = [0, 0]

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            pos = [row, col]

matrix[pos[0]][pos[1]] = '-'

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

total_commands = int(input())

for _ in range(total_commands):
    command = input()
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]

    if not 0 <= dest_row < size or not 0 <= dest_col < size:
        if len(initial_string) >= 1:
            initial_string.pop()
        continue
    if matrix[dest_row][dest_col].isalpha():
        initial_string.append(matrix[dest_row][dest_col])
        matrix[dest_row][dest_col] = '-'
    pos = [dest_row, dest_col]

matrix[pos[0]][pos[1]] = 'P'

print(*initial_string, sep='')
[print(*row, sep='') for row in matrix]