# Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

input_integers = input().split()

for _ in range(len(input_integers)):
    print(input_integers.pop(), end=' ')