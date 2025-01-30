from collections import deque

fuel_stack = [int(x) for x in input().split()]
additional_consumption_deque = deque(int(x) for x in input().split())
fuel_needed_deque = deque(int(x) for x in input().split())
reached_altitudes = []
index = 0

while fuel_needed_deque:
    result = fuel_stack[-1] - additional_consumption_deque[0]
    index += 1
    if result >= fuel_needed_deque[0]:
        fuel_stack.pop()
        additional_consumption_deque.popleft()
        fuel_needed_deque.popleft()
    else:
        print(f"John did not reach: Altitude {index}")
        break
    print(f"John has reached: Altitude {index}")
    reached_altitudes.append(f'Altitude {index}')

if fuel_needed_deque:
    print("John failed to reach the top.")
    if len(reached_altitudes) > 0:
        print('Reached altitudes: ' + ', '.join(reached_altitudes))
    else:
        print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")

