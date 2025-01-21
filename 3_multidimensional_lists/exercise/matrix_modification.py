
matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]


while True:
    command = input().split()
    if command[0] == 'END':
        break
    row, col, value = [int(x) for x in command[1:]]
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]):
        if command[0] == 'Add':
            matrix[row][col] += value
        elif command[0] == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*row) for row in matrix]