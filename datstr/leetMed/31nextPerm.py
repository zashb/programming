import itertools


def nextPerm(n):
    c = itertools.permutations(n, len(n))
    c_s = sorted(c)
    for i, j in enumerate(c_s):
        if j > n and i != len(c_s) - 1:
            return j
        elif j == n and i == len(c_s) - 1:
            return c_s[0]


if __name__ == '__main__':
    print(nextPerm((1, 2, 3)))
    print(nextPerm((3, 2, 1)))
    print(nextPerm((1, 1, 5)))
