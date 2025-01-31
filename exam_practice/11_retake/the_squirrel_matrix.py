size = int(input())
directions = input().split(', ')
matrix = []
pos = [0, 0]
hazelnuts_collected = 0

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}


for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 's':
            pos = [row, col]



for direction in directions:
    dest_row = pos[0] + movement_mapper[direction][0]
    dest_col = pos[1] + movement_mapper[direction][1]
    if not(0 <= dest_row < size and 0<= dest_col < size):
        print("The squirrel is out of the field.")
        break

    if matrix[dest_row][dest_col] == 'h':
        hazelnuts_collected += 1
        matrix[dest_row][dest_col] = '*'
        if hazelnuts_collected >= 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[dest_row][dest_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    pos = [dest_row, dest_col]
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")