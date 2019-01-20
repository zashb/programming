class Solution:
    def powXN(self, num):
        # for i in range(32):
        #     if num == 2 ** i:
        #         return True
        #     if num < 2**i:
        #         break
        #     print(i)
        # return False

        # return any(num==2**i for i in range(32))

        return (num & num-1)==0

print(Solution().powXN(8))
print(Solution().powXN(18))
print(Solution().powXN(140737488355328))
