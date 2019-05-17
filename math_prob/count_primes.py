def count_primes(n):
    if n < 2:
        return 0
    primes = [False, False] + [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


expected = 4
actual = count_primes(10)
print(expected == actual)

expected = 25
actual = count_primes(100)
print(expected == actual)