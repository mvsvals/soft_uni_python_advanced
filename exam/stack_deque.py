from collections import deque

potions =   {
            110: 'Brew of Immortality',
            100: 'Essence of Resilience',
            90: 'Draught of Wisdom',
            80: 'Potion of Agility',
            70:'Elixir of Strength',
}

crafted_potions = []

substances_stack = [int(x) for x in input().split(', ')]
energy_deque = deque(int(x) for x in input().split(', '))

while substances_stack and energy_deque and len(crafted_potions) < 5:
    substance = substances_stack[-1]
    crystal = energy_deque[0]
    result =  substance + crystal
    if result in potions and potions[result] not in crafted_potions:
        crafted_potions.append(potions[result])
        substances_stack.pop()
        energy_deque.popleft()
        del potions[result]
    else:
        for key, value in potions.items():
            if key < result:
                substances_stack.pop()
                energy_deque[0] -= 20
                crafted_potions.append(value)
                del potions[key]
                if energy_deque[0] <= 0:
                    energy_deque.popleft()
                    break
                energy_deque.rotate(-1)
                break
        else:
            substances_stack.pop()
            energy_deque[0] -= 5
            if energy_deque[0] <= 0:
                energy_deque.popleft()
                continue
            energy_deque.rotate(-1)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print('Crafted potions: ' + ', '.join(crafted_potions))

if substances_stack:
    print('Substances: ' + ', '.join(str(x) for x in reversed(substances_stack)))
if energy_deque:
    print('Crystals: ' + ', '.join(str(x) for x in energy_deque))


