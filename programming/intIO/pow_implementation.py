"""
implement pow()
idea : even / odd / -ve powers
comp : O(n)
"""


def pow(a, b):
    neg_flag = True if b < 0 else False
    b = abs(b)
    if b == 0:
        res = 1
    # the return statements are removed because of -1
    elif b == 1:
        res = a
    elif b == 2:
        res = a * a
    elif b % 2 == 0:
        res = pow(a, b // 2) * pow(a, b // 2)
    else:
        res = a * pow(a, b - 1)
    return res if neg_flag == False else 1.0 / res


a, b = 2, 3
expected = 8
actual = pow(a, b)
print(expected == actual)

a, b = 4, -1
expected = 0.25
actual = pow(a, b)
print(expected == actual)
