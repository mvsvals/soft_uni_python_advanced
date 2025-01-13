input_string = input()

stack = []

for index, char in enumerate(input_string):
    if char == '(':
        stack.append(index)
    elif char == ')':
        print(input_string[stack.pop():index + 1])

