def shop_from_grocery_list(budget, grocery_list, *args):
    for product_name, product_price in args:
        if product_name not in grocery_list:
            continue
        if budget >= product_price:
           grocery_list.remove(product_name)
           budget -= float(product_price)
        else:
            break
    return f"Shopping is successful. Remaining budget: {budget:.2f}." if not grocery_list else f"You did not buy all the products. Missing products: " + ', '.join(grocery_list) + '.'

