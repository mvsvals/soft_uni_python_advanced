from collections import deque

water_quantity = int(input())

my_queue = deque()

while True:
    input_string = input()
    if input_string == 'Start':
        break
    my_queue.append(input_string)

while True:
    input_string = input().split()
    if input_string[0] == 'End':
        break
    if input_string[0].isdigit():
        if int(input_string[0]) <= water_quantity:
            print(my_queue.popleft(), 'got water')
            water_quantity -= int(input_string[0])
        else:
            print(my_queue.popleft(), 'must wait')
    elif input_string[0] == 'refill':
        water_quantity += int(input_string[1])

print(f"{water_quantity} liters left")