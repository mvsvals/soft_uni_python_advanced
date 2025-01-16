sequence_one = set(map(int, input().split()))
sequence_two = set(map(int, input().split()))

total_lines = int(input())

for _ in range(total_lines):
    command = input().split()
    action, sequence = command[0], command[1]
    if action == "Add":
        numbers = set(map(int, command[2:]))
        if sequence == "First":
            sequence_one.update(numbers)
        elif sequence == "Second":
            sequence_two.update(numbers)
    elif action == "Remove":
        numbers = set(map(int, command[2:]))
        if sequence == "First":
            sequence_one.difference_update(numbers)
        elif sequence == "Second":
            sequence_two.difference_update(numbers)
    elif command[0] == "Check":
        print(sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one))

print(*sorted(sequence_one), sep=', ')
print(*sorted(sequence_two), sep=', ')