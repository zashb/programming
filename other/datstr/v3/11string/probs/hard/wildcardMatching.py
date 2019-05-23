class Solution:
    def isMatch(self, inpStr, pattern):
        inpStrLen, patternLen = len(inpStr), len(pattern)
        if inpStrLen == 0 and patternLen == 0:
            return True
        if inpStrLen == 0 and patternLen != 0:
            return False
        if pattern.count("*") == patternLen:
            return True
        if patternLen - pattern.count("*") > inpStrLen:
            return False
        dp = [True] + [False] * inpStrLen
        for char in pattern:
            if char != "*":
                for idx in range(inpStrLen, 0, -1):
                    dp[idx] = (char == "?" or inpStr[idx - 1] == char) and dp[idx - 1]
            else:
                for idx in range(1, inpStrLen + 1):
                    dp[idx] = dp[idx] or dp[idx - 1]
            dp[0] = dp[0] and char == "*"
        return dp[inpStrLen]


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "aa"))
    print(Solution().isMatch("aaa", "aa"))
    print(Solution().isMatch("aa", "*"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("aa", "?*"))
    print(Solution().isMatch("ab", "?*"))
    print(Solution().isMatch("aab", "c*a*b"))

    # TTR:
    # if char != "*" , dp[idx]=(char=="?" or inpStr[idx-1]==char) and dp[idx-1]
    # else, dp[idx]=dp[idx] or df[idx-1]
