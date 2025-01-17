
rows, columns = list(map(int, input().split(', ')))
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_sum = -999999
max_submatrix = []

for row in range(rows - 1):
    for col in range(columns - 1):
        current_number = matrix[row][col]
        next_number = matrix[row][col+1]
        number_below = matrix[row+1][col]
        number_diagonal = matrix[row+1][col+1]
        total_sum = current_number + next_number + number_below + number_diagonal
        if total_sum > max_sum:
            max_submatrix = [[current_number, next_number], [number_below, number_diagonal]]
            max_sum = total_sum


print(*max_submatrix[0])
print(*max_submatrix[1])
print(max_sum)
