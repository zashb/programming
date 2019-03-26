class Solution:
    def longestConsecSeq(self, nums):
        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                next = num + 1
                while next in nums:
                    next += 1
                best = max(best, next - num)
        return best


if __name__ == "__main__":
    print(Solution().longestConsecSeq([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecSeq([100, 4, 200, 1, 3, 2, 5, 6, 201, 202, 203, 204, 205]))

    # TTR:
    # build a set for inp nums
    # check if num is the start of the streak then check if next nums are in nums
    # exit the above loop by comparing with best
