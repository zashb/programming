"""
min # of coins to add up to a val
idea: sort descending, while val > d
comp: O(n)
"""


def min_num_coins(val, denom):
    denom.sort(reverse=True)
    # # counter gets initialized with 1 so not a good idea
    # counter = Counter(denom)
    counter = {d: 0 for d in denom}
    for d in denom:
        while val >= d:
            val -= d
            counter[d] += 1
    return sum(counter.values())


val = 93
denom = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
expected = 5
actual = min_num_coins(val, denom)
print(expected == actual)
