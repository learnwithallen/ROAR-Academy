def pascals_triangle(num_rows):
    """Build Pascal's triangle as a list of rows.

    Each row is generated from the previous one, where every interior
    value is the sum of the two values above it.
    """
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """Print the triangle centered, without brackets, commas or padding."""
    rows = [" ".join(str(value) for value in row) for row in triangle]
    width = len(rows[-1]) if rows else 0
    for row in rows:
        print(row.center(width))


if __name__ == "__main__":
    n = 5
    print_triangle(pascals_triangle(n))
