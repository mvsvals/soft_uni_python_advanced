from collections import deque

size = 8
matrix = []
w_pos = []
b_pos = []
is_game_over = False
players = deque(['w', 'b'])

directions = {
    'w': ((-1, -1), (-1, 1)),
    'b': ((1, -1), (1, 1))
}

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'w':
            w_pos = [row, col]
        elif matrix[row][col] == 'b':
            b_pos = [row, col]

positions = {'w': w_pos, 'b': b_pos}

while not is_game_over:
    current = players[0]
    other = players[1]

    current_row, current_col = positions[current]
    other_row, other_col = positions[other]

    for row_movement, col_movement in directions[current]:
        capture_row = current_row + row_movement
        capture_col = current_col + col_movement

        if capture_row == other_row and capture_col == other_col:
            position = f"{chr(97 + capture_col)}{8 - capture_row}"
            print(f"Game over! {'White' if current == 'w' else 'Black'} win, capture on {position}.")
            is_game_over = True
            break

    if is_game_over:
        break

    if current == 'w':
        next_row = current_row - 1
        if next_row == 0:
            position = f"{chr(97 + current_col)}{8 - next_row}"
            print(f"Game over! White pawn is promoted to a queen at {position}.")
            is_game_over = True
            break
    else:
        next_row = current_row + 1
        if next_row == 7:
            position = f"{chr(97 + current_col)}{8 - next_row}"
            print(f"Game over! Black pawn is promoted to a queen at {position}.")
            is_game_over = True
            break

    matrix[current_row][current_col] = '-'
    positions[current][0] = next_row
    matrix[next_row][current_col] = current
    players.rotate()