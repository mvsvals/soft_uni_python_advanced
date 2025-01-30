from collections import deque

worm_stack = [int(x) for x in input().split()]
holes_deque = deque(int(x) for x in input().split())
matches = 0
max_matches = len(worm_stack)

while worm_stack and holes_deque:
    worm = worm_stack[-1]
    hole = holes_deque[0]

    holes_deque.popleft()
    if worm == hole:
        worm_stack.pop()
        matches += 1
    else:
        worm_stack[-1] -= 3
        if worm_stack[-1] <= 0:
            worm_stack.pop()


if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worm_stack:
    if max_matches == matches:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print("Worms left: " + ', '.join(str(x) for x in worm_stack))


if not holes_deque:
    print("Holes left: none")
else:
    print("Holes left: " + ', '.join(str(x) for x in holes_deque))