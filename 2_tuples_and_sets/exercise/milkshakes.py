from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
milk_cups_deque = deque(int(x) for x in input().split(', '))
milkshakes_made = 0

while chocolates_stack and milk_cups_deque and milkshakes_made < 5:
    chocolate = chocolates_stack[-1]
    milk = milk_cups_deque[0]

    if chocolate <= 0 and milk <= 0:
        chocolates_stack.pop()
        milk_cups_deque.popleft()
        continue
    elif chocolate <= 0:
        chocolates_stack.pop()
        continue
    elif milk <= 0:
        milk_cups_deque.popleft()
        continue

    if chocolate == milk:
        chocolates_stack.pop()
        milk_cups_deque.popleft()
        milkshakes_made += 1
    else:
        milk_cups_deque.rotate(-1)
        chocolates_stack[-1] -= 5

if milkshakes_made == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print('Chocolate: ', end='')
if chocolates_stack:
    print(*chocolates_stack, sep=', ')
else:
    print('empty')

print('Milk: ', end='')
if milk_cups_deque:
    print(*milk_cups_deque, sep=', ')
else:
    print('empty')