import unittest


def check_subset_sum(nums, Sum):
    subsets = get_all_subsets(nums)
    for i in subsets:
        if sum(i) == Sum:
            return True
    return False


def get_all_subsets(nums):
    res, temp, start = [], [], 0
    get_all_subsets_util(nums, res, temp, start)
    return res


def get_all_subsets_util(nums, res, temp, start):
    if temp not in res:
        res.append(temp)
    for i in range(start, len(nums)):
        if nums[i] not in temp:
            get_all_subsets_util(nums, res, temp + [nums[i]], i + 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [3, 34, 4, 12, 5, 2]
        Sum = 9
        expected = True
        actual = check_subset_sum(nums, Sum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
