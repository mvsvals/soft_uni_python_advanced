from collections import deque

wasted_water = 0

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]


while bottles and cups:
    bottle_fill_amount = bottles[-1]
    cup_capacity_amount = cups[0]
    if bottle_fill_amount >= cup_capacity_amount:
        cups.popleft()
        wasted_water += bottle_fill_amount - cup_capacity_amount
        bottles.pop()
    else:
        cups[0] -= bottles.pop()

if bottles:
    print('Bottles:', *bottles, sep=' ')
elif cups:
    print('Cups:', *cups, sep=' ')
print(f"Wasted litters of water: {wasted_water}")