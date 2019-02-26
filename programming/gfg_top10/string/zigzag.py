import unittest


def get_zigzag(string, nrows):
    if nrows == 1 or nrows >= len(string):
        return string
    result = [''] * nrows
    rownum, step = 0, 1
    for i in string:
        # decrementing step will not overwrite because we are always appending to the string
        result[rownum] += i
        if rownum == 0:
            step = 1
        elif rownum == nrows - 1:
            step = -1
        rownum += step
    return ''.join(result)


def zigZag(nums):
    flag = True
    for i in range(len(nums) - 1):
        if flag is True:
            # If we have a situation like A > B > C, we get A > B < C by swapping B and C
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            # If we have a situation like A < B < C, we get A < C > B by swapping B and C
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        flag = bool(1 - flag)
    return nums


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string = "PAYPALISHIRING"
        nrows = 3
        expected = "PAHNAPLSIIGYIR"
        actual = get_zigzag(string, nrows)
        self.assertEqual(expected, actual)

    def test_something2(self):
        nums = [4, 3, 7, 8, 6, 2, 1]
        expected = [3, 7, 4, 8, 2, 6, 1]
        actual = zigZag(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
