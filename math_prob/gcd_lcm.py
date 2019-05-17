import math


def get_lcm(a, b):
    return (a * b) / get_gcd_euclidean(a, b)


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


expected = 12
actual = get_gcd(60, 48)
print(expected == actual)

expected = 12
actual = get_gcd_euclidean(60, 48)
print(expected == actual)

expected = 240.0
actual = get_lcm(60, 48)
print(expected == actual)
