class Solution:
    def reverseInt(self, num):
        # cmp num and 0; instead of cmp(num,0)
        # sign = (num>0)-(num<0)
        sign = -1 if num < 0 else 1
        # reversed abs int
        # rev = int(str(sign * num)[::-1])
        rev=int(str(abs(num))[::-1])
        # if rev < 2 **31:
        #     return sign*rev
        # else:
        #     return 0
        return sign * rev if rev < 2 ** 31 else 0


print(Solution().reverseInt(123))
print(Solution().reverseInt(-123))
print(Solution().reverseInt(2 ** 30))
