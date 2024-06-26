#!/usr/bin/python3
"""
A function to generate Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Returns:
        List of lists of integers representing Pascal’s triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous_row = triangle[-1]
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)
    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Prints the Pascal's Triangle.
        """
        for row in triangle:
            print("[{}]".format(",".join(map(str, row))))

    print_triangle(pascal_triangle(5))
