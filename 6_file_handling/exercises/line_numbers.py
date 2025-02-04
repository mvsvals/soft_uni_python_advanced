
with open('6_file_handling/exercises/example.txt') as file:
    lines = file.readlines()

with open('6_file_handling/exercises/example2.txt', 'a') as write_file:
    for index in range(len(lines)):
        total_alpha, total_punct = 0, 0
        for char in lines[index]:
            if char.isalpha():
                total_alpha += 1
            elif char in ['?', '!', '.', ',', "'", '-']:
                total_punct += 1
        lines[index] = lines[index].replace('\n', '')
        write_file.write(f'Line {index + 1}: {lines[index]} ({total_alpha})({total_punct})\n')
