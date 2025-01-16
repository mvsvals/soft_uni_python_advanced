from collections import deque

working_bees_deque = deque(int(x) for x in input().split())
nectar_values_stack = [int(x) for x in input().split()]
symbols_deque = deque(input().split())
total_honey = 0

while working_bees_deque and nectar_values_stack:
    if nectar_values_stack[-1] >= working_bees_deque[0]:
        bee = working_bees_deque.popleft()
        nectar = nectar_values_stack[-1]
        symbol = symbols_deque.popleft()

        if symbol == '/' and nectar == 0:
            nectar_values_stack.pop()
            continue
        nectar_values_stack.pop()
        result = abs(eval(f"{bee} {symbol} {nectar}"))
        total_honey += result
    else:
        nectar_values_stack.pop()

print(f"Total honey made: {total_honey}")
if working_bees_deque:
    print(f"Bees left: {', '.join(map(str, working_bees_deque))}")
if nectar_values_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_values_stack))}")