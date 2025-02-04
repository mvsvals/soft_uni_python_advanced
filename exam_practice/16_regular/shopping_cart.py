def shopping_cart(*args):
    products = 0
    meals = {
            'Soup': {'ingredients': [], 'max_ingredients': 3},
            'Pizza': {'ingredients': [], 'max_ingredients': 4},
            'Dessert': {'ingredients': [], 'max_ingredients': 2}
             }
    for x in args:
        if x == 'Stop':
            break
        meal, ingr = x
        if meals[meal]['max_ingredients'] > len(meals[meal]['ingredients']):
            if ingr not in meals[meal]['ingredients']:
                meals[meal]['ingredients'].append(ingr)
                products += 1
    meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]['ingredients']), x[0])))
    output = []
    for meal, data in meals.items():
        output.append(f"{meal}:")
        for ing in sorted(data['ingredients']):
            output.append(f" - {ing}")
    return '\n'.join(output) if products > 0 else "No products in the cart!"


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))