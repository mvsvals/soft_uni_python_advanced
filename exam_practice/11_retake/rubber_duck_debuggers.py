from collections import deque

time_deque = deque(int(x) for x in input().split())
task_stack = [int(x) for x in input().split()]
duckies_dict = {
                'Darth Vader Ducky': 0,
                'Thor Ducky': 0,
                'Big Blue Rubber Ducky': 0,
                'Small Yellow Rubber Ducky': 0
                }

while time_deque and task_stack:
    result_time = time_deque[0] * task_stack[-1]
    if 0 <= result_time <= 240:
        if 0 <= result_time <= 60:
            duckies_dict['Darth Vader Ducky'] += 1
        elif result_time <= 120:
            duckies_dict['Thor Ducky'] += 1
        elif result_time <= 180:
            duckies_dict['Big Blue Rubber Ducky'] += 1
        elif result_time <= 240:
            duckies_dict['Small Yellow Rubber Ducky'] += 1
        time_deque.popleft()
        task_stack.pop()
    else:
        task_stack[-1] -= 2
        time_deque.rotate(-1)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f'{key}: {value}') for key, value in duckies_dict.items()]