from collections import deque

turn_order = deque(input().split(', '))
penalized = []

matrix = [input().split() for _ in range(6)]

while True:
    command = input().split(', ')
    dest_row, dest_col = int(command[0][1:]), int(command[1][:-1])
    person_turn = turn_order[0]
    if person_turn not in penalized:
        if matrix[dest_row][dest_col] == 'E':
            print(f"{person_turn} found the Exit and wins the game!")
            break
        elif matrix[dest_row][dest_col] == 'T':
            print(f"{person_turn} is out of the game! The winner is {turn_order[1]}.")
            break
        elif matrix[dest_row][dest_col] == 'W':
            print(f"{person_turn} hits a wall and needs to rest.")
            penalized.append(person_turn)
    else:
        penalized.remove(person_turn)
    turn_order.rotate(-1)