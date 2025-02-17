def get_factorial(n:int):
    if n == 1:
        return n
    return n * get_factorial(n - 1)

numbers = int(input())
print(get_factorial(numbers))