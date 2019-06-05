# all possib subsets with dups
# backtracking
import itertools

"""
Idea : BT
Com : O(2 ^ n)
"""


def all_subsets(nums):
    def backtrack(res, tmp, nums, startIdx):
        res.append(tmp[:])
        for i in range(startIdx, len(nums)):
            if i > startIdx and nums[i] == nums[i - 1]:
                continue
            tmp.append(nums[i])
            backtrack(res=res, tmp=tmp, nums=nums, startIdx=i + 1)
            tmp.pop()

    res, temp, startIdx = [], [], 0
    backtrack(res, temp, nums, startIdx)
    return res


# def main(nums):
#     subsets = [[]]
#     for i in sorted(nums):
#         subsets += [j + [i] for j in subsets]
#     subsets = sorted(subsets)
#     return [key for key, group in itertools.groupby(subsets)]


expected = [[], [2], [2, 1], [2, 1, 3], [2, 3], [1], [1, 3], [3]]
actual = all_subsets([2, 1, 3])
print(expected == actual)

expected = [[], [2], [2, 1], [2, 1, 3], [2, 1, 3, 1], [2, 1, 1], [2, 3], [2, 3, 1], [2, 1], [1], [1, 3], [1, 3, 1],
            [1, 1], [3], [3, 1], [1]]
actual = all_subsets([2, 1, 3, 1])
print(expected == actual)

expected = [[], ['a'], ['a', 'b'], ['a', 'b', 'c'], ['a', 'c'], ['b'], ['b', 'c'], ['c']]
actual = all_subsets(list("abc"))
print(expected == actual)
