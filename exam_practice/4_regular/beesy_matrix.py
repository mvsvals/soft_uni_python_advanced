
size = int(input())
matrix = []

bee_pos = [0, 0]
bee_energy = 15
nectar_collected = 0
NECTAR_TARGET = 30

has_reached_hive = False
has_restored_energy = False

direction_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'B':
            bee_pos = [row, col]

matrix[bee_pos[0]][bee_pos[1]] = '-'

while True:
    if bee_energy <= 0:
        if nectar_collected < 30:
            print("This is the end! Beesy ran out of energy.")
            break
        else:
            if has_restored_energy:
                print("This is the end! Beesy ran out of energy.")
                break
            else:
                bee_energy += nectar_collected - NECTAR_TARGET
                nectar_collected = 30
                has_restored_energy = True
                if bee_energy <= 0:
                    print("This is the end! Beesy ran out of energy.")
                    break
    command = input()
    dest_row = bee_pos[0] + direction_mapper[command][0]
    dest_col = bee_pos[1] + direction_mapper[command][1]
    if dest_row < 0:
        dest_row = len(matrix) - 1
    elif dest_row >= size:
        dest_row = 0
    if dest_col < 0:
        dest_col = len(matrix[0]) - 1
    elif dest_col >= size:
        dest_col = 0

    bee_energy -= 1
    bee_pos = [dest_row, dest_col]

    if matrix[bee_pos[0]][bee_pos[1]].isdigit():
        nectar_collected += int(matrix[dest_row][dest_col])
        matrix[bee_pos[0]][bee_pos[1]] = '-'
    elif matrix[bee_pos[0]][bee_pos[1]] == 'H':
        if nectar_collected >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
            break
        else:
            print("Beesy did not manage to collect enough nectar.")
            break



matrix[bee_pos[0]][bee_pos[1]] = 'B'
[print(*row, sep='') for row in matrix]