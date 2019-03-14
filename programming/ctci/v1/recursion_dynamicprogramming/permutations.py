"""
prob : all perm of string
idea : BT, bef,aft ; res = set()
com : O(n!) with dups, O(n^2 n!) without dups; total #perm - n!, this is called n times, since each char to be printed -  * n, overall O(n^2 * n!)
"""


def get_perm(string):
    res = set()
    get_perm_util("", string, res)
    return res


def get_perm_util(prefix, remainder, res):
    if len(remainder) == 0:
        res.add(prefix)
    else:
        n = len(remainder)
        for i in range(n):
            before = remainder[:i]
            c = remainder[i]
            after = remainder[i + 1:]
            get_perm_util(prefix + c, before + after, res)


string = "helo"
actual = get_perm(string)
# len(string) = 4; #perm = 4!; 24
print(len(actual) == 24)

string = "hello"
actual = get_perm(string)
# len(string) = 5; #perm = 5!/2!; 60
print(len(actual) == 60)

# import itertools
# import unittest
#
# class MyTestCase(unittest.TestCase):
#     def test_perm1(self):
#         nums = list(range(1, 4))
#         actual = get_perm1(nums)
#         print(actual)
#
#     def test_perm2(self):
#         nums = list(range(1, 4))
#         actual = get_perm2(nums)
#         print(actual)
#
#     def test_perm3(self):
#         nums = list(range(1, 4))
#         get_perm3(nums, 0, len(nums) - 1)
#
#     def test_permute_dups(self):
#         for case in [[1, 2, 3], [1, 2, 2], "ABC", "AAB"]:
#             actual = permute_dups(case)
#             print(actual)
#
# def permute_dups(nums):
#     ans = [[]]
#     for i in nums:
#         new_ans = []
#         for j in ans:
#             for k in range(len(j) + 1):
#                 new_ans.append(j[:k] + [i] + j[k:])
#                 if k < len(j) and j[k] == i:
#                     break  # handles duplication
#         ans = new_ans
#     return ans
#
#
# def get_perm3(nums, l, r):
#     if l == r:
#         print(nums)
#     else:
#         for i in range(l, r + 1):
#             nums[l], nums[i] = nums[i], nums[l]
#             get_perm3(nums, l + 1, r)
#             nums[l], nums[i] = nums[i], nums[l]
#
#
# def get_perm2(nums):
#     if len(nums) == 0:
#         return []
#     if len(nums) == 1:
#         return [nums]
#     result = []
#     for i in range(len(nums)):
#         m = nums[i]
#         rem_list = nums[:i] + nums[i + 1:]
#         for p in get_perm2(rem_list):
#             result.append([m] + p)
#     return result
#
#
# def get_perm1(nums):
#     perm = itertools.permutations(nums)
#     return list(perm)
#
#
# if __name__ == '__main__':
#     unittest.main()
