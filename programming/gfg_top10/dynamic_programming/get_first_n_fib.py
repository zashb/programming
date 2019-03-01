import unittest


def get_first_n_fib(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 20
        print(get_first_n_fib(n))


if __name__ == '__main__':
    unittest.main()
