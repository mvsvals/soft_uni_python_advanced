from collections import deque

bomb_effect_deque = deque(int(x) for x in input().split(', '))
bomb_casing_stack = [int(x) for x in input().split(', ')]

is_pouch_filled = False

bombs = {
        'Cherry Bombs': [60, 0],
        'Datura Bombs': [40, 0],
        'Smoke Decoy Bombs': [120, 0]
         }

while bomb_casing_stack and bomb_effect_deque and not is_pouch_filled:
    total_sum = bomb_effect_deque[0] + bomb_casing_stack[-1]
    for k, v in bombs.items():
        if total_sum == v[0]:
            bombs[k][1] += 1
            bomb_effect_deque.popleft()
            bomb_casing_stack.pop()
            break
    else:
        bomb_casing_stack[-1] -= 5
    is_pouch_filled = all(y[1] >= 3 for x, y in bombs.items())


if is_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect_deque:
    print("Bomb Effects: " + ', '.join(str(x) for x in bomb_effect_deque))
else:
    print("Bomb Effects: empty")

if bomb_casing_stack:
    print("Bomb Casings: " + ', '.join(str(x) for x in bomb_casing_stack))
else:
    print("Bomb Casings: empty")

for k, v in bombs.items():
    print(f"{k}: {v[1]}")