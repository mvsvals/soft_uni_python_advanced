
def boarding_passengers(capacity, *args):
    output = ["Boarding details by benefit plan:"]
    groups_remaining = len(args)
    boarded_groups = {}
    for total_guests, name in args:
        if capacity >= total_guests:
            if name not in boarded_groups.keys():
                boarded_groups[name] = total_guests
            else:
                boarded_groups[name] += total_guests
            capacity -= total_guests
            groups_remaining -= 1
            if capacity == 0:
                break

    for name, total_guests in sorted(boarded_groups.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"## {name}: {total_guests} guests")
    if groups_remaining == 0:
        output.append("All passengers are successfully boarded!")
    elif capacity <= 0 < groups_remaining:
        output.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif capacity > 0 and groups_remaining > 0:
        output.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return '\n'.join(output)

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
