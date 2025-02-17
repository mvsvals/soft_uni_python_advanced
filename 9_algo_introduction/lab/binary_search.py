def binary_search(numbers, target_number):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle_index = (left + right) // 2
        middle_ele = numbers[middle_index]
        if middle_ele == target_number:
            return middle_index
        if middle_ele < target_number:
            left = middle_index + 1
        else:
            right = middle_index - 1
    return - 1

nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))