import unittest


def get_stock_span(nums):
    # stack has pop and append; pop when less and add it to res; append res always to stack and result
    stack = []
    result = []
    for i in nums:
        res = 1
        while stack and stack[-1][0] <= i:
            res += stack.pop()[1]
        stack.append([i, res])
        result.append(res)
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [10, 4, 5, 90, 120, 80]
        expected = [1, 1, 2, 4, 5, 1]
        actual = get_stock_span(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
