from collections import deque

item_dict = {
            'Patch': 30,
            'Bandage': 40,
            'MedKit': 100
}

created_items = {}

textile_deque = deque(int(x) for x in input().split())
medicine_stack = [int(x) for x in input().split()]

while textile_deque and medicine_stack:
    total_sum = textile_deque[0] + medicine_stack[-1]
    if total_sum in [30, 40, 100]:
        item = ''
        textile_deque.popleft()
        medicine_stack.pop()
        if total_sum == 30:
            item = 'Patch'
        elif total_sum == 40:
            item = 'Bandage'
        elif total_sum == 100:
            item = 'MedKit'
        if item not in created_items:
            created_items[item] = 0
        created_items[item] += 1
    elif total_sum > 100:
        difference = total_sum - 100
        textile_deque.popleft()
        medicine_stack.pop()
        medicine_stack[-1] += difference
        if 'MedKit' not in created_items:
            created_items['MedKit'] = 0
        created_items['MedKit'] += 1
    else:
        textile_deque.popleft()
        medicine_stack[-1] += 10

if not textile_deque and not medicine_stack:
    print("Textiles and medicaments are both empty.")
elif not textile_deque:
    print("Textiles are empty.")
elif not medicine_stack:
    print("Medicaments are empty.")

if created_items:
    for item, amount in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item} - {amount}")

if medicine_stack:
    print(f"Medicaments left: " + ', '.join(str(x) for x in  reversed(medicine_stack)))
if textile_deque:
    print(f"Textiles left: " + ', '.join(str(x) for x in textile_deque))