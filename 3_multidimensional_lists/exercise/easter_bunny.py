field_size = int(input())
matrix = []
initial_bunny_pos = None

for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        if matrix[row][col] == 'B':
            initial_bunny_pos = (row, col)

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
max_eggs  = float('-inf')
max_direction = ""
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_egg_matrix = []
    row = initial_bunny_pos[0] + move[0]
    col = initial_bunny_pos[1] + move[1]
    while 0 <= row < field_size and 0 <= col < field_size:
        if matrix[row][col] == 'X':
            break
        eggs += int(matrix[row][col])
        curr_egg_matrix.append([row, col])
        row += move[0]
        col += move[1]
    if eggs > max_eggs and curr_egg_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_egg_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)