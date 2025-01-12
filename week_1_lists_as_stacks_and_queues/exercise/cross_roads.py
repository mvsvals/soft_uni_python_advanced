from collections import deque

car_queue = deque()
total_cars_passed = 0
has_crashed = False

green_light_duration = int(input())
free_window_duration = int(input())

while not has_crashed:
    input_command = input()
    if input_command == 'END':
        break
    if input_command == 'green':
        current_green_light = green_light_duration
        while car_queue and current_green_light > 0:
            car = car_queue[0]
            if len(car) <= current_green_light:
                current_green_light -= len(car)
                car_queue.popleft()
                total_cars_passed += 1
            else:
                remaining = len(car) - current_green_light
                if remaining <= free_window_duration:
                    car_queue.popleft()
                    total_cars_passed += 1
                else:
                    print("A crash happened!")
                    hit_index = current_green_light + free_window_duration
                    print(f"{car} was hit at {car[hit_index]}.")
                    has_crashed = True
                break
    else:
        car_queue.append(input_command)

if not has_crashed:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")