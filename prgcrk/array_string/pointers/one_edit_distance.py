"""
prob: Given two strings S and T, determine if they are both one edit distance apart
idea: while, count
comp: O(n)
"""


def is_one_edit_distance(s, t):
    if not s or not t:
        return False
    m, n, i, j, count = len(s), len(t), 0, 0, 0
    if abs(m - n) > 1:
        return False
    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            count += 1
            if count > 1:
                return False
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
    if i < m or j < n:
        count += 1
    if count == 1:
        return True
    return False


expected = True
actual = is_one_edit_distance("hell", "hel")
print(expected == actual)
