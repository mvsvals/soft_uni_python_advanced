
input_numbers = tuple([float(num) for num in input().split()])

data = {}
for num in input_numbers:
    data[num] = input_numbers.count(num)

for key, value in data.items():
    print(f'{key} - {value} times')
