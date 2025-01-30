rows, cols = [int(x) for x in input().split(', ')]

matrix = []
ct_pos = [0, 0]
time_remaining = 16
is_bomb_defused = False
is_killed_during_defuse = False
time_needed_for_defuse = 0

move_mapper = {
               'up': (-1, 0),
               'down': (1, 0),
               'left': (0, -1),
               'right': (0, 1)
               }

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'C':
            ct_pos = [row, col]

while time_remaining > 0:
    command = input()
    if command == 'defuse':
        if matrix[ct_pos[0]][ct_pos[1]] == 'B':
           if time_remaining >= 4:
               matrix[ct_pos[0]][ct_pos[1]] = 'D'
               is_bomb_defused = True
               time_remaining -= 4
               break
           else:
               matrix[ct_pos[0]][ct_pos[1]] = 'X'
               is_killed_during_defuse = True
               time_needed_for_defuse = 4 - time_remaining
               break
        else:
            time_remaining -= 2
            if time_remaining <= 0:
                break
    else:
        dest_row = ct_pos[0] + move_mapper[command][0]
        dest_col = ct_pos[1] + move_mapper[command][1]
        if not(0 <= dest_row < rows and 0 <= dest_col < cols):
            time_remaining -= 1
            continue
        if matrix[dest_row][dest_col] == 'T':
            matrix[dest_row][dest_col] = '*'
            print("Terrorists win!")
            break
        else:
            ct_pos = [dest_row, dest_col]
            time_remaining -= 1

if (time_remaining <= 0 and not is_bomb_defused) or is_killed_during_defuse:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {time_needed_for_defuse} second/s.")
elif is_bomb_defused:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time_remaining} second/s remaining.")

for row in matrix:
    print(*row, sep='')