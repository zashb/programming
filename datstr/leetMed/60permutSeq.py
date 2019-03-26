# def permutSeq(n, k):
#     res = []
#     fact = [1]
#     sb = ""
#     sum = 1
#     for i in range(1, n + 1):
#         sum *= i
#         fact.append(sum)
#     for i in range(1, n + 1):
#         res.append(i)
#     k -= 1
#     for i in range(1, n + 1):
#         idx = k // fact[n - i]
#         sb += str(res[idx])
#         res.pop(idx)
#         k -= idx * fact[n - i]
#     return sb

import math


def permutSeq(n, k):
    numbers = list(range(1, n + 1))
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        # index, k = divmod(k, math.factorial(n))
        index, k = k // math.factorial(n), k % math.factorial(n)
        permutation += str(numbers[index])
        # remove handled number
        numbers.remove(numbers[index])

    return permutation


if __name__ == '__main__':
    print(permutSeq(3, 4))
