class Solution:
    def palInt(self, num):
        # sign = (num>0)-(num<0)
        sign = -1 if num < 0 else +1
        # rev = int(str(num * sign)[::-1])
        rev = int(str(abs(num))[::-1])
        return num == sign * rev if num < 2 ** 31 and rev < 2 ** 31 else 0


print(Solution().palInt(121))
print(Solution().palInt(-121))
print(Solution().palInt(123))
print(Solution().palInt(2 ** 29))
