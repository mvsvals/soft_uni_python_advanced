chars_to_replace = ['-', ',', '.', '!', '?']

with open('example.txt') as file:
    lines = file.readlines()

for index in range(0, len(lines), 2):

    for char_to_replace in chars_to_replace:
        lines[index] = lines[index].replace(char_to_replace, '@')
    current_line_words = lines[index].split()
    for w_index in range(len(current_line_words), -1, -1):
        print(current_line_words[w_index], end=' ')
    print()