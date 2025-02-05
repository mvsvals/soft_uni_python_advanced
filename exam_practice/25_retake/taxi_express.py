from collections import deque

customers_deque = deque(int(x) for x in input().split(', '))
taxis_stack = [int(x) for x in input().split(', ')]
total_time = 0

while customers_deque and taxis_stack:
    customer = customers_deque[0]
    taxi = taxis_stack[-1]
    if customer <= taxi:
        total_time += customers_deque.popleft()
    taxis_stack.pop()

if not customers_deque:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join(str(x) for x in customers_deque)}')