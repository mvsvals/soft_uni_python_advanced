
size = int(input())
matrix = []

player_pos = [0, 0]
player_funds = 100
is_jackpot_won = False
is_player_dead = False

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'G':
            player_pos = [row, col]

movement_mapper = {
                    'up': (-1, 0),
                    'down': (1, 0),
                    'left': (0, -1),
                    'right': (0, 1)
}

matrix[player_pos[0]][player_pos[1]] = '-'

while not is_jackpot_won and not is_player_dead:
    command = input()
    if command == 'end':
        break
    dest_row = player_pos[0] + movement_mapper[command][0]
    dest_col = player_pos[1] + movement_mapper[command][1]

    if not(0 <= dest_row < size and 0 <= dest_col < size):
        is_player_dead = True
        continue

    if matrix[dest_row][dest_col] in 'WPJ':
        if matrix[dest_row][dest_col] == 'W':
            player_funds += 100
        elif matrix[dest_row][dest_col] == 'P':
            player_funds -= 200
        elif matrix[dest_row][dest_col] == 'J':
            player_funds += 100000
            is_jackpot_won = True
        matrix[dest_row][dest_col] = '-'

    player_pos = [dest_row, dest_col]
    if player_funds <= 0:
        is_player_dead = True

matrix[player_pos[0]][player_pos[1]] = 'G'

if is_player_dead:
    print("Game over! You lost everything!")
else:
    if is_jackpot_won:
        print(f"You win the Jackpot! End of the game. Total amount: {player_funds}$")
    else:
        print(f"End of the game. Total amount: {player_funds}$")
    [print(*row, sep='') for row in matrix]


