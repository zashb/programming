class Solution:
    def numOfTrailZero(self, num):
        zeroCnt = 0
        while num > 0:
            num //= 5
            zeroCnt += num
        return zeroCnt


print(Solution().numOfTrailZero(5))
print(Solution().numOfTrailZero(100))
print(Solution().numOfTrailZero(4617))
