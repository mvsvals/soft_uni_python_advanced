
matrix = [[int(x) for x in input().split()]for _ in range(int(input().split()[0]))]
largest_matrix = []
largest_sum = -999999

for row in range(len(matrix)  - 2):
    for col in range(len(matrix[row]) - 2):
        current_sum = sum(matrix[row][col:col + 3] + matrix[row + 1][col:col + 3] + matrix[row + 2][col:col + 3])
        if current_sum > largest_sum:
            largest_matrix = [matrix[row][col:col + 3], matrix[row+1][col:col + 3], matrix[row + 2][col:col + 3]]
            largest_sum = current_sum


print(f'Sum = {largest_sum}')
for row in largest_matrix:
    print(*row, sep=' ')




