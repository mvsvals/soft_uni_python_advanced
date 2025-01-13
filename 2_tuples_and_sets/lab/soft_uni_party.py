
total_guests = int(input())
reservations = set()


for _ in range(total_guests):
    reservation = input()
    reservations.add(reservation)

guest_reservations = input()
while guest_reservations != 'END':
    reservations.remove(guest_reservations)
    guest_reservations = input()

reservations = sorted(reservations)

print(len(reservations))
print(*reservations, sep='\n')