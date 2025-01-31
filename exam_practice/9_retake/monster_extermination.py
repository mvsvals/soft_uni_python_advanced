from collections import deque


monster_deque = deque(int(x) for x in input().split(','))
soldiers_stack = [int(x) for x in input().split(',')]
monsters_killed = 0

while monster_deque and soldiers_stack:
    monster = monster_deque[0]
    soldier = soldiers_stack[-1]
    if soldier == monster:
        soldiers_stack.pop()
        monster_deque.popleft()
        monsters_killed += 1
    elif soldier > monster:
        if len(soldiers_stack) > 1:
            difference = soldiers_stack.pop() - monster_deque.popleft()
            soldiers_stack[-1] += difference
        else:
            soldiers_stack[-1] -= monster_deque.popleft()
        monsters_killed += 1
    else:
        monster_deque[0] -= soldiers_stack.pop()
        monster_deque.rotate(-1)

if not monster_deque:
    print("All monsters have been killed!")
if not soldiers_stack:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")