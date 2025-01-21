def boom(row, col, matrix):
    bomb_value = matrix[row][col]
    if bomb_value <= 0:
        return

    for x in range(max(0, row - 1), min(len(matrix), row + 2)):
        for y in range(max(0, col - 1), min(len(matrix), col + 2)):
            if matrix[x][y] > 0:
                matrix[x][y] -= bomb_value


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for bomb in input().split():
    row, col = [int(x) for x in bomb.split(',')]
    boom(row, col, matrix)

alive_cells = sum(1 for row in matrix for cell in row if cell > 0)
sum_cells = sum(cell for row in matrix for cell in row if cell > 0)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_cells}")

[print(*row) for row in matrix]
