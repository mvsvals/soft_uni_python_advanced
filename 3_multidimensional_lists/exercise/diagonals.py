
matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
primary_diag = []
secondary_diag = []


for row in range(len(matrix)):
    primary_diag.append(matrix[row][row])
    secondary_diag.append(matrix[row][len(matrix[row]) - 1 - row])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diag)}. Sum: {sum(primary_diag)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diag)}. Sum: {sum(secondary_diag)}')
