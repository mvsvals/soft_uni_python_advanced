from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_deque = deque(int(x) for x in input().split())
gifts = {}


while magic_deque and materials_stack:
    materials = materials_stack[-1]
    magic = magic_deque[0]
    total_sum = materials + magic
    if total_sum < 100:
        if total_sum % 2 == 0:
            total_sum = materials_stack[-1] * 2 + magic_deque[0] * 3
        else:
            total_sum *= 2
    elif total_sum > 499:
        total_sum /= 2

    if 100 <= total_sum <= 499:
        materials_stack.pop()
        magic_deque.popleft()
        if 100 <= total_sum <= 199:
            present = "Gemstone"
        elif 200 <= total_sum <= 299:
            present = 'Porcelain Sculpture'
        elif 300 <= total_sum <= 399:
            present = 'Gold'
        elif 400 <= total_sum <= 499:
            present = 'Diamond Jewellery'
        if present not in gifts:
            gifts[present] = 0
        gifts[present] += 1
    else:
        materials_stack.pop()
        magic_deque.popleft()

if ('Gemstone' in gifts and 'Porcelain Sculpture' in gifts) or ('Gold' in gifts and 'Diamond Jewellery' in gifts):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_stack:
    print(f'Materials left: ' + ', '.join(str(x) for x in materials_stack))
if magic_deque:
    print(f'Magic left: ' + ', '.join(str(x) for x in magic_deque))

for x, y in sorted(gifts.items()):
    print(f'{x}: {y}')