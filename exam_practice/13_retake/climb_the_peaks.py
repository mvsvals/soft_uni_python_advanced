from collections import deque

food_stack = [int(x) for x in input().split(', ')]
stamina_deque = deque(int(x) for x in input().split(', '))
peaks = deque([['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]])

reached_peaks = []
days = 1

while days < 8 and peaks:
    total_sum = food_stack[-1] + stamina_deque[0]
    peak_value = peaks[0][1]
    if total_sum >= peak_value:
        reached_peaks.append(peaks.popleft()[0])
        food_stack.pop()
        stamina_deque.popleft()
    else:
        food_stack.pop()
        stamina_deque.popleft()
    days += 1

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if reached_peaks:
    print('Conquered peaks:')
    print('\n'.join(reached_peaks))