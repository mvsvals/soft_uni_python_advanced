from collections import deque

ROWS, COLS = [7, 7]

players_info = {player: {'score': 501, 'turns': 0} for player in input().split(', ')}
turns_deque = deque(player for player in players_info)
matrix = [input().split() for _ in range(ROWS)]

while True:
    current_player, next_player = turns_deque
    player_move = input().split(', ')
    dest_row, dest_col = int(player_move[0][1:]), int(player_move[1][:-1])
    players_info[current_player]['turns'] += 1
    if not(0 <= dest_row < ROWS and 0 <= dest_col < COLS):
        turns_deque.rotate(-1)
        continue

    if matrix[dest_row][dest_col].isdigit():
        players_info[current_player]['score'] -= int(matrix[dest_row][dest_col])
    elif matrix[dest_row][dest_col] == 'D':
        row_sum = sum(int(matrix[x][dest_col]) for x in range(ROWS) if matrix[x][dest_col].isdigit())
        col_sum = sum(int(matrix[dest_row][x]) for x in range(COLS) if matrix[dest_row][x].isdigit())
        players_info[current_player]['score'] -= (row_sum + col_sum) * 2
    elif matrix[dest_row][dest_col] == 'T':
        row_sum = sum(int(matrix[x][dest_col]) for x in range(ROWS) if matrix[x][dest_col].isdigit())
        col_sum = sum(int(matrix[dest_row][x]) for x in range(COLS) if matrix[dest_row][x].isdigit())
        players_info[current_player]['score'] -= (row_sum + col_sum) * 3
    elif matrix[dest_row][dest_col] == 'B':
        print(f"{current_player} won the game with {players_info[current_player]['turns']} throws!")
        break
    if players_info[current_player]['score'] <= 0:
        print(f"{current_player} won the game with {players_info[current_player]['turns']} throws!")
        break
    turns_deque.rotate(-1)

