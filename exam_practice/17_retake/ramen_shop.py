from collections import deque

ramen_stack = [int(x) for x in input().split(', ')]
customer_deque = deque(int(x) for x in input().split(', '))

while ramen_stack and customer_deque:
    ramen = ramen_stack[-1]
    customer = customer_deque[0]
    if ramen == customer:
        ramen_stack.pop()
        customer_deque.popleft()
    elif ramen > customer:
        ramen_stack[-1] -= customer_deque.popleft()
    else:
       customer_deque[0] -= ramen_stack.pop()

if not customer_deque:
    print("Great job! You served all the customers.")
    if ramen_stack:
        print(f"Bowls of ramen left: " + ", ".join(str(x) for x in ramen_stack))
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: " + ', '.join(str(x) for x in customer_deque))