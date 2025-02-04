
size = int(input())
racing_number = input()
matrix = []
pos = [0, 0]

tunnel = []
km_passed = 0


movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}


for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'T':
            tunnel.append([row, col])


matrix[pos[0]][pos[1]] = '.'

while True:
    command = input()
    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        break
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]
    if matrix[dest_row][dest_col] in ".F":
        km_passed += 10
        pos = [dest_row, dest_col]
        if matrix[pos[0]][pos[1]] == 'F':
            print(f"Racing car {racing_number} finished the stage!")
            break
    elif matrix[dest_row][dest_col] == 'T':
        km_passed += 30
        index = tunnel.index([dest_row, dest_col])
        matrix[dest_row][dest_col] = '.'
        tunnel.pop(index)
        pos = tunnel.pop()
        matrix[pos[0]][pos[1]] = '.'


print(f"Distance covered {km_passed} km." )
matrix[pos[0]][pos[1]] = 'C'
[print(*row, sep='') for row in matrix]