
size = int(input())
matrix = []

player_pos = [0, 0]
fish_collected = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'S':
            player_pos = [row, col]

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

matrix[player_pos[0]][player_pos[1]] = '-'

while True:
    command = input()
    if command == 'collect the nets':
        break
    dest_row = player_pos[0] + movement_mapper[command][0]
    dest_col = player_pos[1] + movement_mapper[command][1]

    if dest_row < 0:
        dest_row = size - 1
    elif dest_row > size - 1:
        dest_row = 0

    if dest_col < 0:
        dest_col = size - 1
    elif dest_col > size - 1:
        dest_col = 0

    player_pos = [dest_row, dest_col]
    if matrix[dest_row][dest_col].isdigit():
        fish_collected += int(matrix[dest_row][dest_col])
        matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{dest_row},{dest_col}]")
        exit()

if fish_collected >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_collected} tons of fish more.")

if fish_collected > 0:
    print(f"Amount of fish caught: {fish_collected} tons.")

matrix[player_pos[0]][player_pos[1]] = 'S'
[print(*row, sep='') for row in matrix]