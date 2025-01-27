
size = int(input())
matrix = []
is_planet_found = False

player_position = [0, 0]
player_resources = 100

player_moveset = {'up': (-1, 0),
                  'down': (1, 0),
                  'left': (0, -1),
                  'right': (0, 1)}


for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'S':
            player_position = [row, col]

matrix[player_position[0]][player_position[1]] = '.'

while True:
    command = input()
    dest_row = player_position[0] + player_moveset[command][0]
    dest_col = player_position[1] + player_moveset[command][1]
    if not(0 <= dest_row < size and 0 <= dest_col < size):
        print("Mission failed! The spaceship was lost in space.")
        break
    player_resources -= 5
    if matrix[dest_row][dest_col] == 'R':
        player_resources = min(player_resources + 10, 100)
    elif matrix[dest_row][dest_col] == 'M':
        player_resources -= 5
        matrix[dest_row][dest_col] = '.'
    player_position = [dest_row, dest_col]
    if matrix[dest_row][dest_col] == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {player_resources} resources left.")
        is_planet_found = True
        break

    if player_resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break


if not is_planet_found:
    matrix[player_position[0]][player_position[1]] = 'S'

[print(*x) for x in matrix]

