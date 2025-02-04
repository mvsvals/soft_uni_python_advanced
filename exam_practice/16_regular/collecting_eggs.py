from collections import deque

eggs_deque = deque(int(x) for x in input().split(', '))
paper_stack = [int(x) for x in input().split(', ')]

filled_boxes = 0

while eggs_deque and paper_stack:
    egg = eggs_deque[0]
    paper = paper_stack[-1]
    if egg <= 0 or egg == 13:
        eggs_deque.popleft()
        if egg == 13:
            paper_stack[0], paper_stack[-1] = paper_stack[-1], paper_stack[0]
        continue
    if egg + paper <= 50:
        filled_boxes += 1
    eggs_deque.popleft()
    paper_stack.pop()

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_deque:
    print('Eggs left: ' + ', '.join(str(x) for x in eggs_deque))
if paper_stack:
    print('Pieces of paper left: ' + ', '.join(str(x) for x in paper_stack))