size = int(input())
matrix = []

player_pos = [0, 0]
player_health = 100

stars_remaining = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            player_pos = [row, col]
        elif matrix[row][col] == "*":
            stars_remaining += 1

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

matrix[player_pos[0]][player_pos[1]] = '-'
has_immunity = False


while stars_remaining > 0 and player_health > 0:
    command = input()
    if command == 'end':
        break
    dest_row = (player_pos[0] + movement_mapper[command][0]) % size
    dest_col = (player_pos[1] + movement_mapper[command][1]) % size
    if matrix[dest_row][dest_col] == '*':
        stars_remaining -= 1
        matrix[dest_row][dest_col] = '-'
        if stars_remaining == 0:
            print("Pacman wins! All the stars are collected.")
    elif matrix[dest_row][dest_col] == 'G':
        if has_immunity:
            has_immunity = False
        else:
            player_health -= 50
        matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'F':
        has_immunity = True
        matrix[dest_row][dest_col] = '-'


    player_pos = [dest_row, dest_col]


if stars_remaining > 0 >= player_health:
    print(f"Game over! Pacman last coordinates [{player_pos[0]},{player_pos[1]}]")
elif stars_remaining > 0 and player_health > 0:
    print("Pacman failed to collect all the stars.")

print(f"Health: {player_health}")
if stars_remaining > 0:
    print(f"Uncollected stars: {stars_remaining}")

matrix[player_pos[0]][player_pos[1]] = 'P'
[print(*row, sep='') for row in matrix ]