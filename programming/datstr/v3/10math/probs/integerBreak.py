class Solution:
    def integerbreak(self, n):
        if n < 4:
            return n - 1
        else:
            a = (n - 2) // 3
            b = (n - 2) % 3 + 2
            return 3 ** a * b


print(Solution().integerbreak(2))
print(Solution().integerbreak(10))
