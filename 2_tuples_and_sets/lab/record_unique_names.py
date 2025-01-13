
total_names = int(input())

unique_names = {input() for input_name in range(total_names)}
print(*unique_names, sep='\n')