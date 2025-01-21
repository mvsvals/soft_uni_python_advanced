
matrix = [[x for x in input().split()] for _ in range(int(input().split()[0]))]
squares_found = 0

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        unique_chars = {matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]}
        if len(unique_chars) == 1:
            squares_found += 1

print(squares_found)
