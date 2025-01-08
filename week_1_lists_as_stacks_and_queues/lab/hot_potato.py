from collections import deque

input_names = deque(input().split())

n = int(input()) - 1

while len(input_names) > 1:
    input_names.rotate(-n)
    print('Removed', input_names.popleft())

print('Last is', input_names[0])