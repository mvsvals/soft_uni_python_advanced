from collections import deque

petrol_pumps = int(input())
circle_road = deque()


for _ in range(petrol_pumps):
    amount, distance = input().split()
    circle_road.append([int(amount), int(distance)])

start_position = 0
stops = 0

while stops < petrol_pumps:
    current_fuel_in_tank = 0
    for i in range(petrol_pumps):
        current_fuel_in_tank += circle_road[i][0]
        distance_to_next_pump = circle_road[i][1]
        if current_fuel_in_tank <  distance_to_next_pump:
            circle_road.rotate(-1)
            start_position += 1
            stops = 0
            break
        current_fuel_in_tank -= distance_to_next_pump
        stops += 1

print(start_position)
