class Solution:
    def revInt(self, n):
        rev = 0
        while n > 0:
            rem = n % 10
            rev = rev * 10 + rem
            n = n // 10
        print(rev)


if __name__ == "__main__":
    s = Solution()
    s.revInt(123)
