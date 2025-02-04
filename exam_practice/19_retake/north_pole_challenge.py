
rows, cols = [int(x) for x in input().split(', ')]
matrix = []
pos = [0, 0]
total_items_left = 0

collection_dict = {'D': 0, 'G': 0, 'C': 0}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == 'Y':
            pos = [row, col]
        elif matrix[row][col] in 'DGC':
            total_items_left += 1

matrix[pos[0]][pos[1]] = 'x'

movement_mapper =   {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }

while total_items_left:
    command = input().split('-')
    if command[0] == 'End':
        break
    direction, steps = command[0], int(command[1])
    for _ in range(steps):
        if total_items_left == 0:
            break
        dest_row = pos[0] + movement_mapper[direction][0]
        dest_col = pos[1] + movement_mapper[direction][1]
        if dest_row < 0:
            dest_row = rows - 1
        elif dest_row >= rows:
            dest_row = 0
        if dest_col < 0:
            dest_col = cols - 1
        elif dest_col >= cols:
            dest_col = 0
        if matrix[dest_row][dest_col] in 'DGC':
            collection_dict[matrix[dest_row][dest_col]] += 1
            total_items_left -= 1
        pos = [dest_row, dest_col]
        matrix[pos[0]][pos[1]] = 'x'

if total_items_left == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f'- {collection_dict["D"]} Christmas decorations')
print(f'- {collection_dict["G"]} Gifts')
print(f'- {collection_dict["C"]} Cookies')

matrix[pos[0]][pos[1]] = 'Y'
[print(*row) for row in matrix]