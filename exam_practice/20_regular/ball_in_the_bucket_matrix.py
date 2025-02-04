SIZE = 6
MAX_BALLS = 3

total_points = 0
balls_thrown = 0

matrix = [input().split() for _ in range(SIZE)]

for _ in range(MAX_BALLS):
    coordinates_input = input().split(', ')
    row, col = int(coordinates_input[0][1:]), int(coordinates_input[1][:-1])
    if not(0 <= row < SIZE and 0 <= col < SIZE):
        continue
    if matrix[row][col] == 'B':
        sum_column_points = sum(int(matrix[x][col]) for x in range(SIZE) if matrix[x][col].isdigit())
        total_points += sum_column_points
        matrix[row][col] = 0

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    if total_points <= 199:
        prize = 'Football'
    elif total_points <= 299:
        prize = 'Teddy Bear'
    elif total_points >= 300:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
