from collections import deque

vowels_deque = deque(input().split())
consonants_stack = input().split()
is_word_found = False

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels_deque and consonants_stack:
    if is_word_found:
        break
    first_char = vowels_deque[0]
    second_char = consonants_stack[-1]
    for flower, word in flowers.items():
        if first_char in word:
            flowers[flower] = flowers[flower].replace(first_char, '')
        if second_char in word:
            flowers[flower] = flowers[flower].replace(second_char, '')
        if len(flowers[flower]) == 0:
            print(f"Word found: {flower}")
            is_word_found = True
            break
    vowels_deque.popleft()
    consonants_stack.pop()

if not is_word_found:
    print("Cannot find any word!")
if vowels_deque:
    print("Vowels left: " + ' '.join(vowels_deque))
if consonants_stack:
    print('Consonants left: ' + ' '.join(consonants_stack))