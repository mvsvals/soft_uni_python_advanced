rows, columns = list(map(int, input().split(', ')))


matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(columns):
    total_sum = 0
    for row in range(rows):
        total_sum += matrix[row][col]
    print(total_sum)

