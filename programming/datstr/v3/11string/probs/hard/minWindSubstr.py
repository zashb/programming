import collections


class Solution:
    def minWindSubstr(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i, I, J = 0, 0, 0
        for idx, char in enumerate(s):
            missing -= need[char] > 0
            need[char] -= 1
            if not missing:
                while i < idx and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or idx - i <= J - I:
                    I, J = i, idx
        return s[I:J + 1]


if __name__ == "__main__":
    print(Solution().minWindSubstr("ADOBECODEBANC", "ABC"))
