
total_commands = int(input())

parking = set()

for _ in range(total_commands):
    direction, car_number = input().split(', ')
    if car_number not in parking and direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT' and car_number in parking:
        parking.remove(car_number)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")