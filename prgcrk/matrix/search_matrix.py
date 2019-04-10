"""
prob: Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has properties:

1) Integers in each row are sorted from left to right. 2) The first integer of each row is greater than the last integer of the previous row.
For example, consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
idea: midx, midy, l<=r
comp:
"""


def search_matrix(mat, target):
    m, n = len(mat), len(mat[0])
    if not mat or not target or m == 0 or n == 0:
        return False
    l, r = 0, m * n - 1
    while l <= r:
        mid = (l + r) // 2
        midx, midy = mid // n, mid % n
        if mat[midx][midy] == target:
            return True
        if mat[midx][midy] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


expected = True
actual = search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
print(expected == actual)
