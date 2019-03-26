class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words:
            return []
        strLen = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for word in words:
            req[word] = req[word] + 1 if word in req else 1
        result = []
        for i in range(min(k, strLen - t + 1)):
            self._findSubstring(i, i, strLen, k, t, s, req, result)
        return result


if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
