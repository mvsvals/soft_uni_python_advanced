
def accommodate(*args, **kwargs):
    guests_not_admitted = 0
    accomodations_made = {}
    output = []
    groups = args
    rooms = {x.replace('room_', ''): y for x, y in sorted(kwargs.items(), key=lambda x: (x[1], x[0]))}
    for people in groups:
        for name, capacity in rooms.items():
            if people == capacity or capacity > people:
                accomodations_made[name] = people
                del rooms[name]
                break
        else:
            guests_not_admitted += people
    if accomodations_made:
        output.append(f"A total of {len(accomodations_made)} accommodations were completed!")
        for room_number, guests in sorted(accomodations_made.items()):
            output.append(f"<Room {room_number} accommodates {guests} guests>")
    else:
        output.append("No accommodations were completed!")

    if guests_not_admitted > 0:
        output.append(f"Guests with no accommodation: {guests_not_admitted}")
    if rooms:
        output.append(f"Empty rooms: {len(rooms)}")

    return '\n'.join(output)


print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))