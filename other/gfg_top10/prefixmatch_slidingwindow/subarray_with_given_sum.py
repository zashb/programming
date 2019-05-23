import unittest


# def find_subarray_with_given_sum(nums, target):
#     """Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number"""
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if sum(nums[i:j + 1]) == target:
#                 # return "Sum found between indexes {} and {}".format(i, j)
#                 print("Sum found between indexes {} and {}".format(i, j))

def find_subarray_with_given_sum(nums, target):
    """Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number
    idea : map to store cum sum upto i - {sum,no.ofoccurencesofsum}, for every sum encountered, we also determine the number of times the sum (sum-k) has occured already, since it will determine the number of times a subarray with sum k has occured upto the current index. We increment the countcount by the same amount
    """
    counter, n, res, Sum = {0: 1}, len(nums), 0, 0
    for i in range(n):
        Sum += nums[i]
        if Sum - target in counter:
            res += counter[Sum - target]
        counter[Sum] = counter.setdefault(Sum, 0) + 1
    return res


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     nums = [15, 2, 4, 8, 9, 5, 10, 23]
    #     Sum = 23
    #     actual = find_subarray_with_given_sum(nums, Sum)
    #     expected = "Sum found between indexes 1 and 4"
    #     self.assertEqual(actual, expected)

    def test_something_2(self):
        nums = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
        target = 0
        find_subarray_with_given_sum(nums, target)


if __name__ == '__main__':
    unittest.main()
