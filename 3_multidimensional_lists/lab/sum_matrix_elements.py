
matrix = []

rows = int(input().split(', ')[0])
total_sum = 0

for _ in range(rows):
    input_line = list(map(int, input().split(', ')))
    total_sum += sum(input_line)
    matrix.append(input_line)


print(total_sum)
print(matrix)