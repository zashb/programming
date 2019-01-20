class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0], res[1] = False,False
        for i in range(2, n):
            if res[i]:
                for j in range(2, (n - 1) // i + 1):
                    res[i * j] = False
        return sum(res)


print(Solution().countPrimes(10))
