board_size = int(input())
board_matrix = []
knights = []
knights_taken_out = 0

possible_moves = [(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (2, 1), (1, 2)]


def calculate_possible_attacks(row_pos, col_pos):
    attack_count = 0
    for row, col in possible_moves:
        move_row = row + row_pos
        move_col = col + col_pos
        if 0 <= move_row < board_size and 0 <= move_col < board_size:
            if board_matrix[move_row][move_col] == 'K':
                attack_count += 1
    return attack_count


def take_out_the_highest_knight():
    global knights_taken_out
    while True:
        for index, data in enumerate(knights):
            knights[index][0] = calculate_possible_attacks(data[1], data[2])
        if any(x[0] > 0 for x in knights):
            knights.sort(key=lambda x: (x[0], -x[1], -x[2]))
            _, rowy, coly = knights.pop()
            board_matrix[rowy][coly] = '0'
            knights_taken_out += 1
        else:
            print(knights_taken_out)
            break


for row in range(board_size):
    board_matrix.append(list(input()))
    for col in range(board_size):
        if board_matrix[row][col] == 'K':
            knights.append([0, row, col])

take_out_the_highest_knight()
