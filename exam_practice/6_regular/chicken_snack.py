from collections import deque

money_amount_stack = [int(x) for x in input().split()]
food_prices_deque = deque(int(x) for x in input().split())
food_eaten = 0

while money_amount_stack and food_prices_deque:
    money = money_amount_stack[-1]
    food_price = food_prices_deque[0]
    if money <= food_price:
        money_amount_stack.pop()
        food_prices_deque.popleft()
        if money == food_price:
            food_eaten += 1
    elif money > food_price:
        difference = money - food_price
        food_prices_deque.popleft()
        if len(money_amount_stack) > 1:
            money_amount_stack.pop()
            money_amount_stack[-1] += difference
        food_eaten += 1

if food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_eaten == 1:
    print(f"Henry ate: {food_eaten} food.")
elif 1 < food_eaten < 4:
    print(f"Henry ate: {food_eaten} foods.")
elif food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")