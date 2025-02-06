
ROWS = 6
COLUMNS = 7
CONNECT_WINNER_COUNT = 4

direction_mapper = {
    'down': (1, 0),
    'right': (0, 1),
    'up_right': (-1, 1),
    'up_left': (-1, -1)
}

available_spots = {col_index: ROWS-1 for col_index in range(COLUMNS)}

class InvalidColumnNumber(Exception):
    pass

class FullColumnError(Exception):
    pass

def validate_column_choice(player_num, column_choice, available_spots):
    try:
        column = int(column_choice)
        if column < 1 or column > COLUMNS:
            raise InvalidColumnNumber
        available_row = available_spots[column - 1]
        if available_row < 0:
            raise FullColumnError
        return column
    except ValueError:
        print(f"{player_num}, please enter a valid number")
    except InvalidColumnNumber:
        print(f'{player_num}, please enter a number between 1 and 7')
    except FullColumnError:
        print('Please select a column with available spots.')

def obtain_position(player_num, board, available_spots):
    while True:
        data = input(f"{player_num}, please select a column:")
        column = validate_column_choice(player_num, data, available_spots)
        if not column:
            continue
        column_index = column - 1
        return available_spots[column_index], column_index

def is_valid_position(row, col):
    return 0 <= row < ROWS and 0 <= col < COLUMNS

def print_board(board):
    for row in board:
        print(row)

def check_direction_count(current_row_index, current_col_index, row_index_movement, col_index_movement, board, current_player_num, sign):
    count = 0
    for index in range(CONNECT_WINNER_COUNT):
        next_row_index = eval(f'{current_row_index}{sign}{row_index_movement}*{index}')
        next_col_index = eval(f'{current_col_index}{sign}{col_index_movement}*{index}')
        if not is_valid_position(next_row_index, next_col_index):
            return count
        if board[next_row_index][next_col_index] == current_player_num:
            count += 1
        else:
            return count
    return count

def is_winner(current_row_index, current_col_index, board, current_player_num):
    for direction, movement in direction_mapper.items():
        row_index_movement, col_index_movement = movement
        count_direction = check_direction_count(current_row_index, current_col_index, row_index_movement, col_index_movement, board, current_player_num, '+')

        total_count = 1 + count_direction
        if direction != "down":
            opposite_count_direction = check_direction_count(current_row_index, current_col_index,
                                                                      row_index_movement, col_index_movement, board,
                                                                      current_player_num, '-')
            total_count += opposite_count_direction
        if total_count >= CONNECT_WINNER_COUNT:
            return True
    return False

turns = 1
matrix = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

while True:
    print_board(matrix)
    player_num = 1 if turns % 2 != 0 else 2
    row_index, col_index = obtain_position(player_num, matrix, available_spots)
    matrix[row_index][col_index] = player_num
    available_spots[col_index] -= 1
    if turns >= 7:
        if is_winner(row_index, col_index, matrix, player_num):
            print(f'Player {player_num} you won!')
            break
    if ROWS * COLUMNS + 1 == turns:
        print('Board is full. No winner.')
        break
    turns += 1