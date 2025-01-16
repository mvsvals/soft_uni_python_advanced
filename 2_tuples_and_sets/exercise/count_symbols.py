
string_input = input()

for char in sorted(set(string_input)):
    print(f'{char}: {string_input.count(char)} time/s')