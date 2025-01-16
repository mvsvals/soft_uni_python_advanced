n, m = [int(x) for x in input().split()]

common_elements = {int(input()) for x in range(n)} & {int(input()) for x in range(m)}
print(*common_elements, sep='\n')