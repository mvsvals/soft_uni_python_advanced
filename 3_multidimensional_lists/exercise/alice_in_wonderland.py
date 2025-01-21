matrix_size = int(input())
matrix = []
alice_row, alice_col = 0, 0
tea_bags_collected = 0

travel_mapper = {
    'up': lambda x, y: (x - 1, y),
    'down': lambda x, y: (x + 1, y),
    'left': lambda x, y: (x, y - 1),
    'right': lambda x, y: (x, y + 1)
}

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col

while True:
    dest_row, dest_col = travel_mapper[input()](alice_row, alice_col)
    matrix[alice_row][alice_col] = '*'

    if not (0 <= dest_row < matrix_size and 0 <= dest_col < matrix_size):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[dest_row][dest_col] == 'R':
        matrix[dest_row][dest_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    if matrix[dest_row][dest_col].isdigit():
        tea_bags_collected += int(matrix[dest_row][dest_col])
    matrix[dest_row][dest_col] = '*'
    alice_row, alice_col = dest_row, dest_col
    if tea_bags_collected >= 10:
        print("She did it! She went to the party.")
        break

[print(*row) for row in matrix]