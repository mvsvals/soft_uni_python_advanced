import math

size = int(input())
matrix = []
pos = [0, 0]
coins_collected = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "P":
            pos = [row, col]

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}
matrix[pos[0]][pos[1]] = '0'
path = [pos]

while True:
    command = input()
    if command not in movement_mapper:
        continue
    dest_row = (pos[0] + movement_mapper[command][0]) % size
    dest_col = (pos[1] + movement_mapper[command][1]) % size
    if matrix[dest_row][dest_col] == 'X':
        coins_collected /= 2
        coins_collected = math.floor(coins_collected)
        path.append([dest_row, dest_col])
        print(f"Game over! You've collected {coins_collected} coins.")
        break
    elif matrix[dest_row][dest_col].isdigit():
        amount = int(matrix[dest_row][dest_col])
        coins_collected += amount
        matrix[dest_row][dest_col] = '0'
        path.append([dest_row, dest_col])
        if coins_collected > 99:
            print(f"You won! You've collected {coins_collected} coins.")
            break

    pos = [dest_row, dest_col]


print('Your path:')
[print(way) for way in path]

