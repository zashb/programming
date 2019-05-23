import itertools


class Solution:
    def largestNumber(self, nums):
        # get all permutations of size=len(nums)
        allPerm = list(itertools.permutations(nums, len(nums)))
        # print(allPerm)
        pl_join = []
        # for each perm, conv to str and "".join
        for i in allPerm:
            str_i = [str(j) for j in i]
            pl_join.append("".join(str_i))
        # conv each joined str to int and return max of them
        return max([int(i) for i in pl_join])


if __name__ == "__main__":
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
