from collections import deque

tool_deque = deque(int(x) for x in input().split())
substances_stack = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tool_deque and substances_stack and challenges:
    result = tool_deque[0] * substances_stack[-1]
    if result in challenges:
        tool_deque.popleft()
        substances_stack.pop()
        challenges.remove(result)
    else:
        tool_deque[0] += 1
        tool_deque.rotate(-1)
        substances_stack[-1] -= 1
        if substances_stack[-1] == 0:
            substances_stack.pop()


if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tool_deque:
    print('Tools: ' + ', '.join(str(x) for x in tool_deque))
if substances_stack:
    print('Substances: ' + ', '.join(str(x) for x in substances_stack))
if challenges:
    print('Challenges: ' + ', '.join(str(x) for x in challenges))