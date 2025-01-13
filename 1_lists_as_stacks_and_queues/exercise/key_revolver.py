from collections import  deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())

bullets_in_barrel = gun_barrel_size
bullet_cost = 0

while bullets and locks:
    bullet_dmg = bullets.pop()
    bullets_in_barrel -= 1
    bullet_cost += bullet_price
    if bullet_dmg <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    if bullets_in_barrel == 0 and bullets:
        print('Reloading!')
        bullets_in_barrel = gun_barrel_size

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullet_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
