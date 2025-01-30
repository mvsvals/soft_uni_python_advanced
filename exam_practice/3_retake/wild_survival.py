from collections import deque

bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    bee = bees[0]
    bee_eater = bee_eaters[-1]
    bee_strength, bee_eater_strength = bee, bee_eater * 7
    if bee_strength > bee_eater_strength:
        bees[0] -= bee_eaters.pop() * 7
        bees.rotate(-1)
    elif bee_strength < bee_eater_strength:
        bee_eaters[-1] -= (bees.popleft() // 7)
    else:
        bees.popleft()
        bee_eaters.pop()

print("The final battle is over!")

if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print("Bee groups left: ", end='')
    print(*bees, sep=', ')
elif bee_eaters:
    print("Bee-eater groups left: ", end='')
    print(*bee_eaters, sep=', ')
