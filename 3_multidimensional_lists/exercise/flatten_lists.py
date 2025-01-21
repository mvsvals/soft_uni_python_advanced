
my_list = [ele for sublist in [ind_list.split() for ind_list in reversed(input().split('|'))] for ele in sublist]
print(*my_list)

