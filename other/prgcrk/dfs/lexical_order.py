"""
prob: Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
idea:
comp:
"""


# def lexical_order(n):
#     if not n:
#         return n
#     return sorted(range(1, n + 1), key=str)


def lexical_order(n):
    if not n:
        return n
    res = [1]
    while len(res) < n:
        new = res[-1] * 10
        while new > n:
            new //= 10
            new += 1
            while new % 10 == 0:
                new //= 10
        res.append(new)
    return res


expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
actual = lexical_order(13)
print(expected == actual)
