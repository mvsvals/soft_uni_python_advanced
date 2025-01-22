
total_presents = int(input())
matrix_size = int(input())
matrix = []
santa_location = [0, 0]
total_nice_kids = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 'S':
            santa_location = [row, col]
        elif matrix[row][col] == 'V':
            total_nice_kids += 1

nice_kids = total_nice_kids

while total_presents > 0:
    command = input()
    if command == 'Christmas morning':
        break
    row = santa_location[0] + directions[command][0]
    col = santa_location[1] + directions[command][1]
    matrix[santa_location[0]][santa_location[1]] = '-'
    santa_location = [row, col]
    if matrix[row][col] == 'V':
        total_presents -= 1
        nice_kids -= 1
    elif matrix[row][col] == 'C':
        cells = [matrix[row+1][col], matrix[row-1][col], matrix[row][col+1], matrix[row][col-1]]
        for cell in cells:
            if cell in 'VX':
                total_presents -= 1
                if cell == 'V':
                    nice_kids -= 1
            if total_presents == 0:
                break
        matrix[row + 1][col], matrix[row - 1][col], matrix[row][col + 1], matrix[row][col - 1] = '-', '-', '-', '-'

    matrix[row][col] = 'S'
    if total_presents == 0:
        break

if nice_kids > 0 and total_presents == 0:
   print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")