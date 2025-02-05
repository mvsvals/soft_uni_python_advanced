size = int(input())
total_bombs = int(input())
matrix = [list('-' * size) for _ in range(size)]


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

for _ in range(total_bombs):
    mine_coords = input().split(', ')
    row, col = int(mine_coords[0][1:]), int(mine_coords[1][:-1])
    matrix[row][col] = '*'

for row in range(size):
    for col in range(size):
        if matrix[row][col] != "*":
            nearby_mines = 0
            initial_pos = [row, col]
            for move in movement_mapper:
                dest_row = initial_pos[0] + movement_mapper[move][0]
                dest_col = initial_pos[1] + movement_mapper[move][1]
                if not 0 <= dest_row < size or not 0 <= dest_col < size:
                    continue
                if matrix[dest_row][dest_col] == '*':
                    nearby_mines += 1
            matrix[row][col] = nearby_mines

[print(*row) for row in matrix]


