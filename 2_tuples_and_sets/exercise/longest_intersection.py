
total_lines = int(input())
longest_intersection = set()

for _ in range(total_lines):
    #  "{first_start},{first_end}-{second_start},{second_end}"
    input_string = input().split('-')
    first_set_start, first_set_end = input_string[0].split(',')
    second_set_start, second_set_end = input_string[1].split(',')
    current_intersection = set(range(int(first_set_start),int(first_set_end)+1)) & set(range(int(second_set_start),int(second_set_end)+1))
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

longest_intersection = list(map(str, longest_intersection))
print(f"Longest intersection is [{', '.join(longest_intersection)}] with length {len(longest_intersection)}")