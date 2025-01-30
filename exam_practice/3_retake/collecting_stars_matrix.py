
size = int(input())
matrix = []
player_pos = [0, 0]
player_stars = 2
STARS_GOAL = 10

direction_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
                    }

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'P':
            player_pos = [row, col]

matrix[player_pos[0]][player_pos[1]] = '.'

while 1 <= player_stars < 10:
    command = input()
    dest_row = player_pos[0] + direction_mapper[command][0]
    dest_col = player_pos[1] + direction_mapper[command][1]
    if not(0 <= dest_row < size and 0 <= dest_col < size):
        player_pos = [0, 0]
        dest_row, dest_col = [0, 0]
    if matrix[dest_row][dest_col] in '*.':
        if matrix[dest_row][dest_col] == '*':
            player_stars += 1
            matrix[dest_row][dest_col] = '.'
        player_pos = [dest_row, dest_col]
    elif matrix[dest_row][dest_col] == '#':
        player_stars -= 1


if player_stars >= 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")
print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")
matrix[player_pos[0]][player_pos[1]] = 'P'
[print(*x) for x in matrix]