class Solution:
    def powXN(self, num):
        for i in range(32):
            if num == 3 ** i:
                return True
            if num < 3**i:
                break
            print(i)
        return False

print(Solution().powXN(9))
print(Solution().powXN(99))