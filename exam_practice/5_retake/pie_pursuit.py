from collections import deque

contestants_deque = deque(int(x) for x in input().split())
pie_stack = [int(x) for x in input().split()]

while contestants_deque and pie_stack:
    contestant_capacity = contestants_deque[0]
    pies = pie_stack[-1]
    if contestant_capacity >= pies:
        contestants_deque[0] -= pie_stack.pop()
        if contestants_deque[0] == 0:
            contestants_deque.popleft()
        else:
            contestants_deque.rotate(-1)
    else:
        pie_stack[-1] -= contestants_deque.popleft()
        if pie_stack[-1] == 1 and len(pie_stack) > 1:
            remainder = pie_stack.pop()
            pie_stack[-1] += remainder

if not pie_stack and contestants_deque:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left: ", end='')
    print(*contestants_deque, sep=', ')
elif not pie_stack and not contestants_deque:
    print("We have a champion!")
elif not contestants_deque and pie_stack:
    print("Our contestants need to rest!")
    print("Pies left: ", end='')
    print(*pie_stack, sep=', ')