from collections import deque

elves = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]
index = 0
toys = 0
total_energy = 0

while elves and materials:
    elf = elves[0]
    material = materials[-1]

    if elf < 5:
        elves.popleft()
        continue

    index += 1
    current_material = material
    produced_toys = 1
    cookie_reward = 1

    if index % 3 == 0:
        current_material *= 2
        produced_toys = 2

    if index % 5 == 0:
        produced_toys = 0
        cookie_reward = 0

    if elf >= current_material:
        elves[0] = elf - current_material + cookie_reward
        materials.pop()
        toys += produced_toys
        total_energy += current_material
    else:
        elves[0] *= 2

    elves.rotate(-1)

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if elves:
    print('Elves left: ' + ', '.join(str(x) for x in elves))
if materials:
    print('Boxes left: ' + ', '.join(str(x) for x in materials))