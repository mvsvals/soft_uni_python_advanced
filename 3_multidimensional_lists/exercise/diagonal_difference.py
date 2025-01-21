
matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
difference = 0

for row in range(len(matrix)):
    difference += matrix[row][row] - matrix[row][len(matrix[row]) - 1 - row]

print(abs(difference))

