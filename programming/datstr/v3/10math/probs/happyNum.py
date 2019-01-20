class Solution:
    def isHappyNum(self, num):
        # split
        # sum of square
        # if sum of square ==1 ret True
        # else repeat
        split = [int(i) for i in str(num)]
        sos = sum([i ** 2 for i in split])
        # print(sos)
        if sos != 1:
            return self.isHappyNum(sos)
        else:
            return True


print(Solution().isHappyNum(19))
