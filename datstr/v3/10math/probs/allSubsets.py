import itertools


class Solution:
    def allSubsets(self, nums):
        # result = []
        # for i in range(len(nums)+1):
        #     # += implies extend
        #     result+=list(itertools.combinations(sorted(nums), i))
        # return result

        subsets = [[]]
        for i in sorted(nums):
            subsets += [j + [i] for j in subsets]
        subsets = sorted(subsets)
        return [key for key, group in itertools.groupby(subsets)]


print(Solution().allSubsets([1, 2, 3]))
print(Solution().allSubsets([1, 2, 2]))
