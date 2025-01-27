from collections import deque

strength_values_stack = [int(x) for x in input().split()]
accuracy_values_queue = deque(int(x) for x in input().split())
goals_scored = 0

while strength_values_stack and accuracy_values_queue:
    strength_value = strength_values_stack[-1]
    accuracy_value = accuracy_values_queue[0]
    total_sum = accuracy_value + strength_value
    if total_sum < 100:
        if strength_value < accuracy_value:
            strength_values_stack.pop()
        elif strength_value > accuracy_value:
            accuracy_values_queue.popleft()
        else:
            accuracy_values_queue.popleft()
            strength_values_stack[-1] = total_sum
    elif total_sum == 100:
        strength_values_stack.pop()
        accuracy_values_queue.popleft()
        goals_scored += 1
    else:
        strength_values_stack[-1] = strength_value - 10
        accuracy_values_queue.rotate(-1)


if goals_scored == 0:
    print("Paul failed to score a single goal.")
elif 0 < goals_scored < 3:
    print("Paul failed to make a hat-trick.")
elif goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored > 3:
    print("Paul performed remarkably well!")

if goals_scored > 0:
    print(f"Goals scored: {goals_scored}")

if strength_values_stack:
    print('Strength values left: ', end='')
    print(*strength_values_stack, sep=', ')

if accuracy_values_queue:
    print('Accuracy values left: ', end='')
    print(*accuracy_values_queue, sep=', ')
