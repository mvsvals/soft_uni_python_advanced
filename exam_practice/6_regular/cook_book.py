def cookbook(*args):
    recipes = {}
    for name, cuisine, ingredients in args:
        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append([name, ingredients])

    recipes = dict(sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0])))
    output = []
    for cuisine, data in recipes.items():
        output.append(f"{cuisine} cuisine contains {len(recipes[cuisine])} recipes:")
        for name, ingredients in sorted(data, key=lambda x: x[0]):
             output.append(f"  * {name} -> Ingredients: " + ', '.join(x for x in ingredients))
    return '\n'.join(output)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))