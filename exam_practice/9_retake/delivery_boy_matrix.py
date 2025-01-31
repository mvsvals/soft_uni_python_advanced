
rows, cols = [int(x) for x in input().split()]
matrix = []
pos = [0, 0]


movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'B':
            pos = [row, col]

initial_pos = pos.copy()

while True:
    command = input()
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]

    if not(0 <= dest_row < rows and 0 <= dest_col < cols):
        print("The delivery is late. Order is canceled.")
        matrix[initial_pos[0]][initial_pos[1]] = ' '
        break

    if matrix[dest_row][dest_col] == '*':
        continue
    elif matrix[dest_row][dest_col] == 'A':
        print("Pizza is delivered on time! Next order...")
        matrix[dest_row][dest_col] = 'P'
        break
    elif matrix[dest_row][dest_col] == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[dest_row][dest_col] = 'R'
    elif matrix[dest_row][dest_col] == '-':
        matrix[dest_row][dest_col] = '.'
    pos = [dest_row, dest_col]

[print(*x, sep='') for x in matrix]