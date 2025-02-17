def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        min_idx = i
        for curr_idx in range(i + 1, len(numbers)):
            if numbers[curr_idx] < numbers[min_idx]:
                min_idx = curr_idx
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

numbers = [int(x) for x in input().split()]
print(selection_sort(numbers))