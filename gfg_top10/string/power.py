"""
implement pow()
"""
import unittest


def pow(a, b):
    negative = True if b < 0 else False
    b = abs(b)
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b == 2:
        return a * a
    if b % 2 == 0:
        res = pow(a, b // 2) * pow(a, b // 2)
    else:
        res = a * pow(a, b - 1)
    return 1.0 / res if negative else res


class Test(unittest.TestCase):
    def test(self):
        a, b = 2, 3
        expected = 8
        actual = pow(a, b)
        print(expected == actual)
