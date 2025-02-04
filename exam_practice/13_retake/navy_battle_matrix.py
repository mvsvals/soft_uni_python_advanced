
size = int(input())
matrix = []
pos = [0, 0]
cruisers_remaining = 3
hp_remaining = 3

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}


for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'S':
            pos = [row, col]

matrix[pos[0]][pos[1]] = '-'

while cruisers_remaining > 0 and hp_remaining > 0:
    command = input()
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]
    if matrix[dest_row][dest_col] == '*':
        hp_remaining -= 1
        matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'C':
        cruisers_remaining -= 1
        matrix[dest_row][dest_col] = '-'
    pos = [dest_row, dest_col]

if hp_remaining == 0:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{pos[0]}, {pos[1]}]!")
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[pos[0]][pos[1]] = 'S'
[print(*row, sep='') for row in matrix]