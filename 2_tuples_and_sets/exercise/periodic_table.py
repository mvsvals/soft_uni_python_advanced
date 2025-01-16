
line_count = int(input())
compounds = set()

for _ in range(line_count):
    compound_input = input().split()
    compounds.update(compound_input)

print(*compounds, sep='\n')