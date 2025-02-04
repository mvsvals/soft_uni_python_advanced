from collections import deque

caffeine_max = 300
caffeine_current = 0

caffeine_stack = [int(x) for x in input().split(', ')]
energy_drinks_deque = deque(int(x) for x in input().split(', '))

while caffeine_stack and energy_drinks_deque:
    result = caffeine_stack[-1] * energy_drinks_deque[0]
    if result + caffeine_current <= caffeine_max:
        caffeine_current += result
        caffeine_stack.pop()
        energy_drinks_deque.popleft()
    else:
        caffeine_stack.pop()
        energy_drinks_deque.rotate(-1)
        caffeine_current = max(0, caffeine_current - 30)

if energy_drinks_deque:
    print(f"Drinks left: " + ", ".join(str(x) for x in energy_drinks_deque))
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_current} mg caffeine.")