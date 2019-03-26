class Solution:
    def distinctSubsequence(self,S,T):
        ways = [0 for _ in range(len(T)+1)]
        ways[0] = 1
        for s in S:
            for j,t in reversed(list(enumerate(T))):
                if s == t:
                    ways[j+1] += ways[j]
        return ways[len(T)]


print(Solution().distinctSubsequence("rabbbit","rabbit"))