from collections import deque


rows, columns = [int(x) for x in input().split()]
snake_string = deque(input())
snake_matrix = []

for row in range(rows):
    snake_matrix.append([''] * columns)
    for col in range(columns):
        symbol = snake_string.popleft()
        snake_string.append(symbol)
        if row % 2 == 0:
            snake_matrix[row][col] = snake_string[0]
        else:
            snake_matrix[row][-1 - col] = snake_string[0]
        snake_string.rotate(-1)

for row in snake_matrix:
    print(*row, sep='')



