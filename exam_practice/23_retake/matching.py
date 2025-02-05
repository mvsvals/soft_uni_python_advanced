from collections import deque

males_stack = [int(x) for x in input().split()]
females_deque = deque(int(x) for x in input().split())
matches = 0

while males_stack and females_deque:
    male = males_stack[-1]
    female = females_deque[0]
    if male <= 0:
        males_stack.pop()
        continue
    if female <= 0:
        females_deque.popleft()
        continue
    if male % 25 == 0:
        males_stack.pop()
        if len(males_stack) >= 1:
            males_stack.pop()
        continue
    if female % 25 == 0:
        females_deque.popleft()
        if len(females_deque) >= 1:
            females_deque.popleft()
        continue
    if male == female:
        females_deque.popleft()
        males_stack.pop()
        matches += 1
    else:
        females_deque.popleft()
        males_stack[-1] -= 2

print(f"Matches: {matches}")

if not males_stack:
    print("Males left: none")
else:
    print("Males left: " + ', '.join(str(x) for x in reversed(males_stack)))

if not females_deque:
    print("Females left: none")
else:
    print("Females left: " + ', '.join(str(x) for x in females_deque))