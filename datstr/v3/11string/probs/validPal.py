class Solution:
    def validPal(self, s):
        isAlnumList = [i.lower() for i in s if i.isalnum()]
        return isAlnumList == isAlnumList[::-1]


if __name__ == "__main__":
    print(Solution().validPal("A man, a plan, a canal: Panama"))
    print(Solution().validPal("race a car"))

# TTR:
# ignoring punctuation by is.alnum()