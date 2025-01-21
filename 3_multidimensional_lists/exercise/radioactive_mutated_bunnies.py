def get_player_position(lair):
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == 'P':
                return i, j
    return None


def get_bunny_positions(lair):
    bunnies = []
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == 'B':
                bunnies.append((i, j))
    return bunnies


def spread_bunnies(lair):
    bunnies = get_bunny_positions(lair)
    rows, cols = len(lair), len(lair[0])

    for row, col in bunnies:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if lair[new_row][new_col] != 'B':
                    lair[new_row][new_col] = 'N'

    for i in range(rows):
        for j in range(cols):
            if lair[i][j] == 'N':
                lair[i][j] = 'B'


def is_valid_position(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def move(direction, pos):
    moves = {
        'L': lambda x, y: (x, y - 1),
        'R': lambda x, y: (x, y + 1),
        'U': lambda x, y: (x - 1, y),
        'D': lambda x, y: (x + 1, y)
    }
    return moves[direction](*pos)


rows, cols = map(int, input().split())
lair = [list(input()) for _ in range(rows)]
commands = input()
player_row, player_col = get_player_position(lair)
won = False
dead = False
final_pos = (player_row, player_col)

for command in commands:
    if not (won or dead):
        # Remove player from current position
        lair[player_row][player_col] = '.'

        # Calculate new position
        new_row, new_col = move(command, (player_row, player_col))

        # Check if player won
        if not is_valid_position(new_row, new_col, rows, cols):
            won = True
            final_pos = (player_row, player_col)
        else:
            # Update player position
            player_row, player_col = new_row, new_col
            final_pos = (player_row, player_col)

            # Check if player died
            if lair[player_row][player_col] == 'B':
                dead = True
            else:
                lair[player_row][player_col] = 'P'

        spread_bunnies(lair)

        if not won and lair[player_row][player_col] == 'B':
            dead = True

for row in lair:
    print(''.join(row))

if won:
    print(f"won: {final_pos[0]} {final_pos[1]}")
else:
    print(f"dead: {final_pos[0]} {final_pos[1]}")