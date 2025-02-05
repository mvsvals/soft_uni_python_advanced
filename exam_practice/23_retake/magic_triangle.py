def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        prev_row = triangle[i - 1]
        curr_row = []
        for j in range(i + 1):
            left = prev_row[j - 1] if j > 0 else 0
            right = prev_row[j] if j < len(prev_row) else 0
            curr_row.append(left + right)

        triangle.append(curr_row)

    return triangle

print(get_magic_triangle(5))