def main(n):
    if n < 3:   return 0
    primes = [False,False]+[True]*(n-2)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:   primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)

if __name__ == '__main__':
    print(main(10))