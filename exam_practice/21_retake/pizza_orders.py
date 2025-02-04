from collections import deque

orders_deque = deque(int(x) for x in input().split(', '))
workers_stack = [int(x) for x in input().split(', ')]
total_pizzas_made = 0

while orders_deque and workers_stack:
    order = orders_deque[0]
    worker = workers_stack[-1]
    if order <= 0 or order > 10:
        orders_deque.popleft()
        continue
    if order <= worker:
        workers_stack.pop()
        total_pizzas_made += orders_deque.popleft()
    else:
        pizzas = workers_stack.pop()
        orders_deque[0] -= pizzas
        total_pizzas_made += pizzas


if not orders_deque:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_pizzas_made}')
    print(f'Employees: ' + ', '.join(str(x) for x in workers_stack))
else:
    print("Not all orders are completed.")
    print("Orders left: " + ", ".join(str(x) for x in orders_deque))