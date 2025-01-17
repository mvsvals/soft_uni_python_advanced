
matrix = [[int(ele) for ele in input().split(', ')] for _ in range(int(input()))]

print([element for sublist in matrix for element in sublist])