
expression_input = input()
my_stack = []

expression_mapper = {
    '(': ')',
    '{': '}',
    '[': ']'
}

for char in expression_input:
    if char in expression_mapper.keys():
        my_stack.append(char)
    else:
        if not my_stack:
            print('NO')
            break
        elif char != expression_mapper[my_stack[-1]]:
            print('NO')
            break
        else:
            my_stack.pop()
else:
    if my_stack:
        print('NO')
    else:
        print('YES')