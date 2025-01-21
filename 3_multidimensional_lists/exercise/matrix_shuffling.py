def is_valid_position(row_one, col_one, row_two, col_two):
    return 0 <= row_one < len(matrix) and 0 <= row_two < len(matrix) and 0 <= col_one <= len(matrix[0]) and 0 <= col_two <= len(matrix[0])


rows, columns = list(map(int, input().split()))

matrix = [[ele for ele in input().split()] for _ in range(rows)]

while True:
    input_command = input().split()
    if input_command[0] == 'END':
        break
    is_valid_command = input_command[0] == 'swap' and len(input_command) == 5
    if not is_valid_command:
        print('Invalid input!')
        continue
    else:
        row_one, col_one = int(input_command[1]), int(input_command[2])
        row_two, col_two = int(input_command[3]), int(input_command[4])
        if is_valid_position(row_one, col_one, row_two, col_two):
            matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        else:
            print('Invalid input!')
            continue
        for row in matrix:
            print(*row, sep=" ")


