class Solution:
    def lengthOfLongestNonRepSubstr(self, s):
        # lp, rp, maxLen = 0, 1, 0
        # while rp < len(s):
        #     if s[rp] not in s[lp:rp]:
        #         rp += 1
        #     else:
        #         if len(s[lp:rp]) > maxLen:
        #             maxLen = len(s[lp:rp])
        #         lp = rp
        # return maxLen

        # lp, rp, notRepLen = 0, 1, []
        # while rp < len(s):
        #     if s[rp] not in s[lp:rp]:
        #         rp += 1
        #     else:
        #         notRepLen.append(len(s[lp:rp]))
        #         lp = rp
        # return max(notRepLen)

        lp, nonRepListLengths = 0, []
        for rp in range(lp + 1, len(s)):
            if s[rp] in s[lp:rp]:
                nonRepListLengths.append(len(s[lp:rp]))
                lp = rp
            else:
                continue
        return max(nonRepListLengths)


if __name__ == "__main__":
    print(Solution().lengthOfLongestNonRepSubstr("abcabcbb"))
    print(Solution().lengthOfLongestNonRepSubstr("bbbbbb"))
    print(Solution().lengthOfLongestNonRepSubstr("pwwkew"))

    # TTR:
    # set lp=rp after appending the list len
