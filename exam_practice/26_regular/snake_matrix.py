
size = int(input())
matrix = []
pos = [0, 0]
burrows_pos = []
total_food = 0
is_outside = False

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'S':
            pos = [row, col]
        elif matrix[row][col] == 'B':
            burrows_pos.append([row, col])

matrix[pos[0]][pos[1]] = '.'

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

while True:
    command = input()
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]
    if not(0 <= dest_row < size and 0 <= dest_col < size):
        print("Game over!")
        is_outside = True
        break
    if matrix[dest_row][dest_col] == '*':
        total_food += 1
    elif matrix[dest_row][dest_col] == 'B':
        matrix[dest_row][dest_col] = '.'
        burrows_pos.remove([dest_row, dest_col])
        dest_row, dest_col = burrows_pos[0]
    pos = [dest_row, dest_col]
    matrix[pos[0]][pos[1]] = '.'

    if total_food >= 10:
        print("You won! You fed the snake.")
        break

if not is_outside:
    matrix[pos[0]][pos[1]] = 'S'
print(f"Food eaten: {total_food}")
[print(*x, sep='') for x in matrix]