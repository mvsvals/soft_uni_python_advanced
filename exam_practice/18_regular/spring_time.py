def start_spring(**kwargs):
    output = []
    item_catalogue = {category: [animal_name for animal_name, animal_type in kwargs.items() if animal_type == category] for category in set(kwargs.values())}
    item_catalogue = sorted(item_catalogue.items(), key=lambda x: (-len(x[1]), x[0]))
    for category, animals in item_catalogue:
        output.append(f'{category}:')
        for animal in sorted(animals):
            output.append(f'-{animal}')

    return '\n'.join(output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))