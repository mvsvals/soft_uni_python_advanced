
total_lines = int(input())
even_set, odd_set = set(), set()

for line_number in range(1, total_lines+1):
    input_name = input()
    name_ascii_sum = sum(ord(char) for char in input_name) // line_number
    if name_ascii_sum % 2 == 0:
        even_set.add(name_ascii_sum)
    else:
        odd_set.add(name_ascii_sum)


if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*even_set.symmetric_difference(odd_set), sep=', ')
