def forecast(*args):
    locations = {'Sunny': [], 'Cloudy': [], 'Rainy': []}
    for location, weather in sorted(args, key=lambda x: x[0]):
        locations[weather].append(location)
    return '\n'.join(f"{location} - {weather}" for weather, locations in locations.items() for location in locations)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))