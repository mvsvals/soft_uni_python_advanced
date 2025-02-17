def bubble_sort(numbers):
    is_sorted = False
    sorted_elements = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(numbers) - sorted_elements):
            i = j - 1
            if numbers[i] > numbers[j]:
                is_sorted = False
                numbers[i], numbers[j] = numbers[j], numbers[i]
        sorted_elements += 1

numbers = [int(x) for x in input().split()]
print(bubble_sort(numbers))
print(*numbers)