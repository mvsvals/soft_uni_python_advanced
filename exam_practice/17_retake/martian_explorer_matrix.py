size = 6
matrix = []
pos = [0, 0]
deposits_found = set()

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'E':
            pos = [row, col]

commands = input().split(', ')

movement_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for command in commands:
    dest_row = pos[0] + movement_mapper[command][0]
    dest_col = pos[1] + movement_mapper[command][1]

    # Fix the wrapping logic using modulo
    dest_row = dest_row % size
    dest_col = dest_col % size

    # Check current position
    if matrix[dest_row][dest_col] in 'WMC':
        resource = {
            'W': 'Water',
            'M': 'Metal',
            'C': 'Concrete'
        }[matrix[dest_row][dest_col]]
        print(f"{resource} deposit found at ({dest_row}, {dest_col})")
        deposits_found.add(resource)
    elif matrix[dest_row][dest_col] == 'R':
        print(f"Rover got broken at ({dest_row}, {dest_col})")
        break

    pos = [dest_row, dest_col]

if len(deposits_found) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")