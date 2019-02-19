import unittest


def ngfe(nums):
    n = len(nums)
    if n <= 0:
        print("List empty")
        return []
    stack = [0] * n
    freq = {}
    for i in nums:
        if i in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    res = [0] * n
    top = -1
    top += 1
    stack[top] = 0
    for i in range(1, n):
        if freq[nums[stack[top]]] > freq[nums[i]]:
            top += 1
            stack[top] = i

        else:
            while top > -1 and freq[nums[stack[top]]] < freq[nums[i]]:
                res[stack[top]] = nums[i]
                top -= 1
            top += 1
            stack[top] = i
    while top > -1:
        res[stack[top]] = -1
        top -= 1
    return res


class MyTestCase(unittest.TestCase):
    def test_ngfe(self):
        nums = [1, 1, 2, 3, 4, 2, 1]
        actual = ngfe(nums)
        print(actual)
