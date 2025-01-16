from collections import deque


input_string = deque(x for x in input().split())
colors_dic = {'orange': ['red', 'yellow'],
              'purple': ['red', 'blue'],
              'green': ['yellow', 'blue']}

colors = ['orange', 'purple', 'green', 'red', 'yellow', 'blue']
output = []

while input_string:
    concatenated_string = input_string[0] if len(input_string) < 2 else input_string[0] + input_string[-1]
    reversed_concatenated_string = input_string[0] if len(input_string) < 2 else input_string[-1] + input_string[0]

    if concatenated_string in colors or reversed_concatenated_string in colors:
        if len(input_string) > 1:
            output.append(input_string.popleft() + input_string.pop() if concatenated_string in colors else input_string.pop() + input_string.popleft())
        else:
            output.append(input_string.pop())
    else:
        if len(input_string) % 2 == 0:
            index = len(input_string) // 2
        else:
            index = len(input_string) // 2 + 1

        if len(input_string[-1]) > 1:
            input_string[-1] = input_string[-1][:len(input_string[-1]) - 1]
            input_string.insert(index, input_string.pop())
        else:
            input_string.pop()

        if len(input_string) > 0:
            if len(input_string[0]) > 1:
                input_string[0] = input_string[0][:len(input_string[0]) - 1]
                input_string.insert(index, input_string.popleft())
            elif len(input_string) > 1:
                input_string.popleft()



for color in output:
    if color in colors_dic.keys():
        required_colors = colors_dic[color]
        if not all(subcolor in output for subcolor in required_colors):
            output.remove(color)

print(output)
