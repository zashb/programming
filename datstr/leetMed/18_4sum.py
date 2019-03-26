import itertools


def foursum(n, t):
    c = itertools.combinations(n, 4)
    return [i for i in c if sum(i) == t]


if __name__ == "__main__":
    print(foursum([1, 0, -1, 0, -2, 2], 0))
