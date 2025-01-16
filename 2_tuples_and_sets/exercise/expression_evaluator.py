from functools import reduce

number_list = []

for list_element in input().split():
    if list_element in '*+-/':
        number_list = [reduce(lambda x,y: eval(f'{x} {list_element if list_element != "/" else "//"} {y}'), number_list)]
    else:
        number_list.append(int(list_element))

print(number_list[0])
