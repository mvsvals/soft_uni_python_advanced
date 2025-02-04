from collections import deque

seat_matches = []
rotations = 0

seats = {x: False for x in input().split(', ')}
my_deque = deque(int(x) for x in input().split(', '))
my_stack = [int(x) for x in input().split(', ')]

while rotations < 10 and len(seat_matches) < 3:
    rotations += 1
    ascii_char = chr(my_deque[0] + my_stack[-1])
    first_ticket, second_ticket = str(my_deque[0]) + ascii_char, str(my_stack[-1]) + ascii_char
    if any(x in seats for x in [first_ticket, second_ticket]):
        if first_ticket in seats:
            ticket_matched = first_ticket
        else:
            ticket_matched = second_ticket
        my_deque.popleft()
        my_stack.pop()
        if seats[ticket_matched]:
            continue
        seats[ticket_matched] = True
        seat_matches.append(ticket_matched)

    else:
        my_deque.rotate(-1)
        my_stack.insert(0, my_stack.pop())

print(f"Seat matches: " + ', '.join(seat_matches))
print(f"Rotations count: {rotations}")