def stock_availability(inventory_list, action, *args):
    if action == 'delivery':
        inventory_list.extend(args)
    elif action == 'sell':
        if not args:
            inventory_list.pop(0)
        elif isinstance(args[0], int):
            return inventory_list[args[0]:] if args[0] < len(inventory_list) else []
        else:
            for item in args:
                while item in inventory_list:
                    inventory_list.remove(item)
    return inventory_list

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
