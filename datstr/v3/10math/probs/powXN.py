class Solution:
    def powXN(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.powXN(x, -n)
        if n % 2:
            return x * self.powXN(x, n - 1)
        return self.powXN(x * x, n / 2)


print(Solution().powXN(2, 3))
print(Solution().powXN(2, -2))
