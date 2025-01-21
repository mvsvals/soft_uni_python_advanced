
minefield_size = int(input())

commands = input().split()

matrix = []
coal_remaining = 0

command_mapper = {
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1),
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y)
}

for row in range(minefield_size):
    matrix.append([x for x in input().split()])
    for col in range(minefield_size):
        if matrix[row][col] == 's':
            player_row_pos, player_col_pos = (row, col)
        elif matrix[row][col] == 'c':
            coal_remaining += 1


for command in commands:
    next_player_row, next_player_col = command_mapper[command](player_row_pos, player_col_pos)
    is_move_valid = 0 <= next_player_row < len(matrix) and 0 <= next_player_col < len(matrix)
    if not is_move_valid:
        continue
    player_row_pos, player_col_pos = next_player_row, next_player_col
    if matrix[player_row_pos][player_col_pos] == 'c':
        coal_remaining -= 1
        matrix[player_row_pos][player_col_pos] = '*'
    elif matrix[player_row_pos][player_col_pos] == 'e':
        print(f"Game over! ({player_row_pos}, {player_col_pos})")
        exit()

if coal_remaining:
    print(f"{coal_remaining} pieces of coal left. ({player_row_pos}, {player_col_pos})")
else:
    print(f"You collected all coal! ({player_row_pos}, {player_col_pos})")
