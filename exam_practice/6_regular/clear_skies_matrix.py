
size = int(input())
matrix = []

player_pos = [0, 0]
player_hp = 300
enemy_airplanes_remaining = 4

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'J':
            player_pos = [row, col]


movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

matrix[player_pos[0]][player_pos[1]] = '-'

while player_hp > 0 and enemy_airplanes_remaining > 0:
    command = input()
    dest_row = player_pos[0] + movement_mapper[command][0]
    dest_col = player_pos[1] + movement_mapper[command][1]

    if matrix[dest_row][dest_col] == 'R':
        player_hp= 300
        matrix[dest_row][dest_col] = '-'
    elif matrix[dest_row][dest_col] == 'E':
        matrix[dest_row][dest_col] = '-'
        if enemy_airplanes_remaining == 1:
            print("Mission accomplished, you neutralized the aerial threat!")
            enemy_airplanes_remaining -= 1
        else:
            player_hp -= 100
            if player_hp <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{dest_row}, {dest_col}]!")
            else:
                enemy_airplanes_remaining -= 1

    player_pos = [dest_row, dest_col]

matrix[player_pos[0]][player_pos[1]] = 'J'
[print(*row, sep='') for row in matrix]