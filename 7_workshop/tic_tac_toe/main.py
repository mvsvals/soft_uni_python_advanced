class InvalidPositionNumber(Exception):
    pass

class PositionAlreadyTaken(Exception):
    pass

def obtain_valid_position(player, matrix, position_mapper):
    while True:
        try:
            selected_position = int(input(f'{player}, please select a spot:'))
            if 1 > selected_position or selected_position > 9:
                raise InvalidPositionNumber
            pos_row, pos_col = position_mapper[selected_position]
            if matrix[pos_row][pos_col] != " ":
                raise PositionAlreadyTaken
            return selected_position
        except ValueError:
            print('Please enter a valid number')
        except InvalidPositionNumber:
            print('Please enter a number between 1 and 9')
        except PositionAlreadyTaken:
            print('Please select an empty position')

def is_winner(player_symbol, matrix):
    matrix_length = len(matrix)
    for row in matrix:
        if all(el == player_symbol for el in row):
            return True
    for col_index in range(matrix_length):
        if all(matrix[row_index][col_index] == player_symbol for row_index  in range(matrix_length)):
            return True
    diagonals_winner = (all(matrix[index][index] == player_symbol for index in range(matrix_length)) or
                        all(matrix[matrix_length - 1 - col_index][col_index] == player_symbol for col_index in range(matrix_length)))
    if diagonals_winner:
        return True
    return False

def print_board(matrix):
    for row in matrix:
        print(f"|  {'  |  '.join(row)}  | ")

def play_turn(player_symbol, row, col, matrix, turns_count):
    matrix[row][col] = player_symbol
    if turns_count >= 5:
        return is_winner(player_symbol, matrix)
    print_board(matrix)

def save_game_result(winner_name):
    with open('result.txt') as file:
        lines = file.readlines()
    content = ''
    is_new = True
    for line in lines:
        name,score = line.split(',')
        score = score[:-1]
        if name.lower() == winner_name.lower():
            score = int(score) + 1
            is_new = False
        content += f'{name},{score}\n'
    if is_new:
        content += f'{winner_name},1\n'
    with open('result.txt', 'w') as file:
        file.write(content)

def play():
    player_one_name = input('Player One, enter your name:')
    player_two_name = input('Player Two, enter your name:')

    symbol = input('Player One, select your symbol - either X or O:')
    while True:
        if symbol not in ['X', 'x', 'O', 'o']:
            symbol = input()
        else:
            break

    player_one_symbol = symbol.upper()
    player_two_symbol = "0" if player_one_symbol == 'X' else 'X'

    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    for row in board:
        print(f'| {"  |  ".join(row)}  |')

    print(f'{player_one_name} starts first')

    position_mapper = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }

    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_to_symbol_mapper = {player_one_name: player_one_symbol,
                               player_two_name: player_two_symbol}

    turns_count = 1
    while True:
        current_player_name = player_two_name if turns_count % 2 == 0 else player_one_name
        position = obtain_valid_position(current_player_name, matrix, position_mapper)
        row, col = position_mapper[position]
        player_symbol = player_to_symbol_mapper[current_player_name]
        winner = play_turn(player_symbol, row, col, matrix, turns_count)
        if winner:
            print_board(matrix)
            print(f'{current_player_name} is winner!')
            save_game_result(current_player_name)
            break
        turns_count += 1
        if turns_count == 10:
            print_board(matrix)
            print('No winner - game over!')

            break

def show_stats():
    with open('results.txt') as file:
        for row in file.readlines():
            print(row, end='')

if __name__ == '__main__':
    command = input()
    while True:
        if command == 'stats':
            show_stats()
            break
        elif command == 'play':
            play()
            break
        elif command == 'end':
            exit(0)
        else:
            command = input("Please select between stats, play and end.")