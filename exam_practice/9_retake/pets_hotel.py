def accommodate_new_pets(capacity, weight_limit, *args):
    dogs_dict = {}
    output = []
    for pet_type, pet_weight in args:
        if capacity <= 0:
            output.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > weight_limit:
            continue
        if not pet_type in dogs_dict:
            dogs_dict[pet_type] = 0
        dogs_dict[pet_type] += 1
        capacity -= 1
    else:
        output.append(f'All pets are accommodated! Available capacity: {capacity}.')
    output.append("Accommodated pets:")
    for pet_type, weight in sorted(dogs_dict.items(), key=lambda x: x[0]):
        output.append(f'{pet_type}: {dogs_dict[pet_type]}')
    return '\n'.join(output)
