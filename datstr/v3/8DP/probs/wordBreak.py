class Solution:
    def wordBreak(self,s,words):
        d = [False]*len(s)
        for i in range(len(s)):
            for j in words:
                if j ==s[i-len(j)+1:i+1] and (d[i-len(j)] or i-len(j)==-1):
                    d[i]=True

        return d[-1]


if __name__=="__main__":
    print(Solution().wordBreak("leetcode",["leet","code"]))
    print(Solution().wordBreak("leetcode",["le","etcode"]))
    print(Solution().wordBreak("leetcode",["le","tcode"]))