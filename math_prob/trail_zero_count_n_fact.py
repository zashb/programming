def trail_zero_count_n_fact(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res


expected = 1
actual = trail_zero_count_n_fact(5)
print(expected == actual)

expected = 24
actual = trail_zero_count_n_fact(100)
print(expected == actual)
