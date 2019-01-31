import itertools
import unittest


class MyTestCase(unittest.TestCase):
    def test_perm1(self):
        nums = list(range(1, 4))
        actual = get_perm1(nums)
        print(actual)

    def test_perm2(self):
        nums = list(range(1, 4))
        actual = get_perm2(nums)
        print(actual)

    def test_perm3(self):
        nums = list(range(1, 4))
        get_perm3(nums, 0, len(nums) - 1)

    def test_permute_dups(self):
        for case in [[1, 2, 3], [1, 2, 2]]:
            actual = permute_dups(case)
            print(actual)


def permute_dups(nums):
    ans = [[]]
    for i in nums:
        new_ans = []
        for j in ans:
            for k in range(len(j) + 1):
                new_ans.append(j[:k] + [i] + j[k:])
                if k < len(j) and j[k] == i:
                    break  # handles duplication
        ans = new_ans
    return ans


def get_perm3(nums, l, r):
    if l == r:
        print(nums)
    else:
        for i in range(l, r + 1):
            nums[l], nums[i] = nums[i], nums[l]
            get_perm3(nums, l + 1, r)
            nums[l], nums[i] = nums[i], nums[l]


def get_perm2(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i + 1:]
        for p in get_perm2(rem_list):
            result.append([m] + p)
    return result


def get_perm1(nums):
    perm = itertools.permutations(nums)
    return list(perm)


if __name__ == '__main__':
    unittest.main()
