
matrix = [[x for x in list(input())] for _ in range(int(input()))]
symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if symbol == matrix[row][col]:
            print(f'({row}, {col})')
            exit()

print(f"{symbol} does not occur in the matrix")