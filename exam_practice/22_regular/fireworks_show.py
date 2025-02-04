from collections import deque

firework_effects_deque = deque(int(x) for x in input().split(', '))
explosive_power_stack = [int(x) for x in input().split(', ')]
fireworks_made = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

while firework_effects_deque and explosive_power_stack and not all(x[1] >= 3 for x in fireworks_made.items()):
    firework = firework_effects_deque[0]
    explosives = explosive_power_stack[-1]
    if firework <= 0:
        firework_effects_deque.popleft()
        continue
    if explosives <= 0:
        explosive_power_stack.pop()
        continue
    total_sum = firework + explosives
    if total_sum % 3 == 0 or total_sum % 5 == 0:
        if total_sum % 5 == 0 and total_sum % 3 == 0:
            fireworks_made['Crossette Fireworks'] += 1
        elif total_sum % 3 == 0:
            fireworks_made['Palm Fireworks'] += 1
        elif total_sum % 5 == 0 and total_sum % 3 != 0:
            fireworks_made['Willow Fireworks'] += 1

        firework_effects_deque.popleft()
        explosive_power_stack.pop()
    else:
        firework_effects_deque[0] -= 1
        firework_effects_deque.rotate(-1)

if all(x[1] >= 3 for x in fireworks_made.items()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects_deque:
    print("Firework Effects left: " + ', '.join(str(x) for x in firework_effects_deque))
if explosive_power_stack:
    print("Explosive Power left: " + ', '.join(str(x) for x in explosive_power_stack))

for x, y in fireworks_made.items():
    print(f'{x}: {y}')