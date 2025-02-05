
SIZE = 8
matrix = []

k_pos = [0, 0]
qs_pos = []

winning_queens = []

movement_mapper = {
                    'up': (-1, 0),
                    'up-left': (-1, -1),
                    'up-right': (-1, 1),
                    'down': (1, 0),
                    'down-left': (1, -1),
                    'down-right': (1, 1),
                    'left': (0, -1),
                    'right': (0, 1)
}

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == 'K':
            k_pos = [row, col]
        elif matrix[row][col] == 'Q':
            qs_pos.append([row, col])

for i in range(len(qs_pos)):
    initial_queen_pos = qs_pos[i]
    for possible_move in movement_mapper:
        queen_pos = initial_queen_pos
        while True:
            dest_row = queen_pos[0] + movement_mapper[possible_move][0]
            dest_col = queen_pos[1] + movement_mapper[possible_move][1]
            if not 0 <= dest_row < SIZE or not 0 <= dest_col < SIZE or matrix[dest_row][dest_col] == 'Q':
                break
            if matrix[dest_row][dest_col] == 'K':
                winning_queens.append(initial_queen_pos)
                break
            queen_pos = [dest_row, dest_col]


if not winning_queens:
    print('The king is safe!')
else:
    [print(x) for x in winning_queens]