from collections import deque

packages_stack = [int(x) for x in input().split()]
couriers_deque = deque(int(x) for x in input().split())
delivered_packages_weight = 0

while packages_stack and couriers_deque:
    package = packages_stack[-1]
    courier = couriers_deque[0]
    if courier > package:
        couriers_deque[0] -= package * 2
        if couriers_deque[0] > 0:
            couriers_deque.rotate(-1)
        else:
            couriers_deque.popleft()
        delivered_packages_weight += packages_stack.pop()
    elif courier == package:
        delivered_packages_weight += couriers_deque.popleft()
        packages_stack.pop()
    else:
        available_capacity = couriers_deque.popleft()
        delivered_packages_weight += available_capacity
        packages_stack[-1] -= available_capacity

print(f"Total weight: {delivered_packages_weight} kg")
if not packages_stack and not couriers_deque:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_stack and not couriers_deque:
    print("Unfortunately, there are no more available couriers to deliver the following packages: ", end='')
    print(*packages_stack, sep=', ', end='')
elif couriers_deque and not packages_stack:
    print("Couriers are still on duty: ", end='')
    print(*couriers_deque, sep=', ', end='')
    print(" but there are no more packages to deliver.")