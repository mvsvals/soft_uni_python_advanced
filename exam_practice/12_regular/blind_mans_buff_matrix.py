rows, cols = [int(x) for x in input().split()]
matrix = []
pos = [0, 0]
opponents_touched = 0
moves_made = 0

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}


for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == 'B':
            pos = [row, col]



while opponents_touched < 3:
    command = input()
    if command == 'Finish':
        break
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]
    if not(0 <= dest_row < rows and 0<= dest_col < cols) or matrix[dest_row][dest_col] == "O":
        continue

    if matrix[dest_row][dest_col] == 'P':
        opponents_touched += 1
        matrix[dest_row][dest_col] = '-'
    moves_made += 1
    pos = [dest_row, dest_col]

print("Game over!")
print(f"Touched opponents: {opponents_touched} Moves made: {moves_made}")