from collections import deque

toys_mapper = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_presents = []

material_boxes_stack = [int(x) for x in input().split()]
magic_values_deque = deque(int(x) for x in input().split())

while material_boxes_stack and magic_values_deque:
    material = material_boxes_stack[-1]
    magic = magic_values_deque[0]

    if material == 0 or magic == 0:
        if material == 0:
            material_boxes_stack.pop()
        if magic == 0:
            magic_values_deque.popleft()
        continue

    result = material * magic

    if result in toys_mapper:
        crafted_presents.append(toys_mapper[result])
        material_boxes_stack.pop()
        magic_values_deque.popleft()
    elif result < 0:
        sum_of_values = material + magic
        material_boxes_stack.pop()
        magic_values_deque.popleft()
        material_boxes_stack.append(sum_of_values)
    else:
        magic_values_deque.popleft()
        material_boxes_stack[-1] += 15


task_done = ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)

print("The presents are crafted! Merry Christmas!" if task_done else "No presents this Christmas!")

if material_boxes_stack:
    print(f"Materials left: {', '.join(str(x) for x in reversed(material_boxes_stack))}")
if magic_values_deque:
    print(f"Magic left: {', '.join(str(x) for x in magic_values_deque)}")

for toy in sorted(set(crafted_presents)):
    print(f"{toy}: {crafted_presents.count(toy)}")