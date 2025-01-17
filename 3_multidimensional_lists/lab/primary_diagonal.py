
matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

total_sum = 0

for index in range(len(matrix)):
    total_sum += matrix[index][index]

print(total_sum)