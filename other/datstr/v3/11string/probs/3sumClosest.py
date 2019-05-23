import itertools


class Solution:
    def threeSumClosest(self, nums, target):
        # d = {}
        # # get all 3 sums
        # for i in list(itertools.combinations(nums, 3)):
        #     d[sum(i)] = None
        # # map the 3 sum to diff from target
        # for i in d:
        #     d[i] = abs(target - i)
        # # return sum corresp to min diff
        # d = {v: k for k, v in d.items()}
        # return d[min(d)]

        # shorter version of the above
        # d = {}
        # for i in list(itertools.combinations(nums, 3)):
        #     d[sum(i)] = abs(target - sum(i))
        # print(d)
        # return [k for k, v in d.items() if v == min(d.values())]

        # cleaner version
        threeCombs = itertools.combinations(nums,3)
        threeCombs_sums = [sum(i) for i in threeCombs]
        distDict = {abs(i-target):i for i in threeCombs_sums}
        return distDict[min(distDict)]

        # nums = sorted(nums)
        # res = sum(nums[:3])
        # for i, j in enumerate(nums):
        #     lp, rp = i + 1, len(nums) - 1
        #     while lp < rp:
        #         localSum = sum((j, nums[lp], nums[rp]))
        #         if abs(localSum - target) < abs(res - target):
        #             res = localSum
        #         if localSum < target:
        #             lp += 1
        #         elif localSum > target:
        #             rp -= 1
        #         else:
        #             return res
        # return res


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

    # TTR
    # itertools.combinations(nums,3)
    # dict of sum : abs(target-sum)
    # swap k,v d= {v,k for k,v in d.items()}
    # min(d) gives min key
