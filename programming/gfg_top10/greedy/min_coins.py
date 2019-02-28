import unittest


def min_coins(value, denom):
    """we have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the value?"""
    denom.sort()
    n = len(denom)
    result = {i: 0 for i in denom}
    # reversed bec min # of coins
    for i in reversed(denom):
        while value >= i:
            value = value - i
            result[i] = result[i] + 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        value = 93
        denom = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
        print(min_coins(value, denom))


if __name__ == '__main__':
    unittest.main()
