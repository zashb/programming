import unittest


class Test(unittest.TestCase):
    def test_something(self):
        for i in [0.625, 0.72]:
            print(to_binary(i))


def to_binary(n):
    if n >= 1 or n <= 0:
        return "ERROR"
    result = "."
    fraction = 0.5
    while n > 0:
        if len(result) > 32:
            return "ERROR"
        b = n * 2
        if b >= 1:
            result += "1"
            n = b - 1

        else:
            result += "0"
            n = b
    return result


if __name__ == '__main__':
    unittest.main()
