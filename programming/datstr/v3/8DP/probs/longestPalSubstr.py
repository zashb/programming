class Solution:
    def longestPalSubstr(self, s):
        if len(s) == 0:
            return 0
        # rem this var
        maxLen = 1
        start = 0
        res = []
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        res.append(s[start:start + maxLen])
        res.append(maxLen)
        return res


if __name__ == "__main__":
    print(Solution().longestPalSubstr("dpabbad"))
    print(Solution().longestPalSubstr("abca"))
