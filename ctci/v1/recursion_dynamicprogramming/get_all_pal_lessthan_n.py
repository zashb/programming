# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         n = 100002
#         get_all_pal(n)
#
#
# def get_all_pal(n):
#     for j in range(2):
#         i = 1
#         while createPalindrome(i, j % 2) < n:
#             print(createPalindrome(i, j % 2), end=", ")
#             i = i + 1
#
#
# def createPalindrome(inp, isOdd):
#     n = inp
#     result = inp
#     if isOdd:
#         n //= 10
#     while n > 0:
#         result = result * 10 + (n % 10)
#         n //= 10
#     return result
#
#
# if __name__ == '__main__':
#     unittest.main()


import unittest


def get_all_pal_lt_n(n):
    result = []
    for i in range(n):
        if is_pal(i):
            result.append(i)
    return result


def is_pal(n):
    # # using strings
    # return str(n) == str(n)[::-1]
    # # not using strings
    rev = 0
    while n > rev:
        rev = rev * 10 + n % 10
        n = n // 10
    return n == rev or n == rev / 10


class Test(unittest.TestCase):
    def test_get_all_pal_lt_n(self):
        n = 102
        actual = get_all_pal_lt_n(n)
        print(actual)
