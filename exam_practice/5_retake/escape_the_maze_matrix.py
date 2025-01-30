
size = int(input())
matrix = []
player_pos = [0, 0]
player_hp = 100
is_exit_found = False

movement_mapper =   {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            player_pos = [row, col]


matrix[player_pos[0]][player_pos[1]] = '-'

while player_hp > 0 and not is_exit_found:
    command = input()
    dest_row = player_pos[0] + movement_mapper[command][0]
    dest_col = player_pos[1] + movement_mapper[command][1]

    if not(0 <= dest_row < size and 0 <= dest_col < size):
        continue

    if matrix[dest_row][dest_col] == 'M':
        player_hp -= 40
        if player_hp > 0:
            matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'H':
        player_hp = min(100, player_hp + 15)
        matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'X':
        is_exit_found = True
    player_pos = [dest_row, dest_col]

if player_hp <= 0:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {max(0, player_hp)} units")
matrix[player_pos[0]][player_pos[1]] = 'P'
[print(*row, sep='') for row in matrix]