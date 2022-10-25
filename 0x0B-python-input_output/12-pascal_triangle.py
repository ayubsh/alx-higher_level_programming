#!/usr/bin/python3
""" Pascla's triangle """


def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal’s triangle
    Args:
        n: number rows
   """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    new_row = [1]
    res = pascal_triangle(n - 1)
    l_row = res[-1]
    for i in range(len(l_row) - 1):
        num = l_row[i] + l_row[i + 1]
        new_row.append(num)

    new_row.append(1)
    res.append(new_row)
    return res
