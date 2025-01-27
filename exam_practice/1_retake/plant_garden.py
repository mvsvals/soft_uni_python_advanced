
def plant_garden(space:float, *args, **kwargs):
    allowed_plant_types = dict(args)
    planting_requests = dict(sorted(kwargs.items()))
    available_space = space
    planted_plants = []
    output = []

    planting_requests = {key: value for key, value in planting_requests.items() if key in allowed_plant_types.keys()}

    for plant, amount in planting_requests.items():
        plant_space_required = allowed_plant_types[plant]
        total_space_required = plant_space_required * amount

        if total_space_required <= available_space:
            planted_plants.append(f'{plant}: {int(amount)}')
            available_space -= total_space_required
            planting_requests[plant] = 0
        else:
            possible_plants = int(available_space // plant_space_required)
            if possible_plants == 0:
                continue
            planted_plants.append(f'{plant}: {possible_plants}')
            planting_requests[plant] -= possible_plants
            available_space -= plant_space_required * possible_plants

    if all(x == 0 for x in planting_requests.values()):
        output.append(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    else:
        output.append("Not enough space to plant all requested plants!")
    output.append('Planted plants:')
    return '\n'.join(output) + '\n' + '\n'.join(sorted(planted_plants))

print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))