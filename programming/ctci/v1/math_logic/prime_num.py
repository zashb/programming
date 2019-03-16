"""
prob : check is prime
idea : **0.5
com : O(n)
"""


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True


n = 17
expected = True
actual = is_prime(n)
print(expected == actual)

n = 18
expected = False
actual = is_prime(n)
print(expected == actual)

# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         test_cases = [(3, 7, 9)]
#         for case in test_cases:
#             print(is_prime(case))
#
#     def test_soe(self):
#         """Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number"""
#         test_cases = [10, 20, 100]
#         for case in test_cases:
#             print("\nprime nums upto {}".format(case))
#             get_soe(case)
#
#     def test_primenum_upto_n(self):
#         """Given a number N, the task is to print all prime numbers less than or equal to N."""
#         """Time Complexity: O(N3/2) The best solution is to use Sieve of Eratosthenes. The time complexity is O(√N * loglog(N))"""
#         test_cases = [10, 20, 100]
#         for case in test_cases:
#             get_primes_upto(case)
#
#
# def get_primes_upto(n):
#     print("\nprime nums upto : {}".format(n))
#     for i in range(2, n + 1):
#         if is_prime_normal(i):
#             print(i, end=",")
#
#
# def is_prime_normal(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if not n % i:
#             return False
#     return True
#
#
# def get_soe(n):
#     prime = [True for _ in range(n + 1)]
#     p = 2
#     while p <= int(n ** 0.5) + 1:
#         if prime[p]:
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     for p in range(2, n):
#         if prime[p]:
#             print(p, end=",")
#
#
# def is_prime(tuple):
#     result = {}
#     for i in tuple:
#         if i < 2:
#             result[i] = False
#         else:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     result[i] = False
#             if i not in result:
#                 result[i] = True
#     return result
#
#
# if __name__ == '__main__':
#     unittest.main()
