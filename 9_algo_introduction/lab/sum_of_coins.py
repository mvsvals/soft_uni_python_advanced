def choose_coins(coins, target):
    coins.sort(reverse=True)
    used_coins = {}
    index = 0
    while target != 0  and index < len(coins):
        coins_count = target  // coins[index]
        target %= coins[index]
        if coins_count > 0:
            used_coins[coins[index]] = coins_count

        index += 1
    if target != 0:
        return 'Error'
    result = f'Number of coins to take: {sum(used_coins.values())}\n'
    for value, quantity in used_coins.items():
        result += f"{quantity} coin(s) with value {value}\n"
    return result.strip()

coin_list = [int(x) for x in input().split(', ')]
target = int(input())

print(choose_coins(coin_list, target))