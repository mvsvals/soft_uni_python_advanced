
rows, columns = [int(x) for x in input().split()]

for row in range(rows):
    for col in range(columns):
        print(chr(row+97) + chr(row+col+97) + chr(row + 97), end=' ')
    print()



