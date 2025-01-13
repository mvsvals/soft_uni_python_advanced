from collections import deque

total_food = int(input())

orders = deque(int(order_amount) for order_amount in input().split())
print(max(orders))

while orders:
    if orders[0] <= total_food:
        total_food -= orders.popleft()
    else:
        break

if not orders:
    print('Orders complete')
else:
    print('Orders left:', *orders)
