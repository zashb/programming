import math
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_cases = [(60, 48)]
        for case in test_cases:
            print("gcd from math : {}".format(get_gcd(*case)))
            print("gcd from euclidean : {}".format(get_gcd_euclidean(*case)))
            print("lcm : {}".format(get_lcm(*case)))


def get_lcm(a, b):
    return (a * b) / get_gcd(a, b)


def get_gcd(a, b):
    return math.gcd(a, b)


def get_gcd_euclidean(a, b):
    # gcd = sys.maxsize
    gcd = float('inf')
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


if __name__ == '__main__':
    unittest.main()
