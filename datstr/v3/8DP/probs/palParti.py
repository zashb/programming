class Solution:
    def palPart(self, s):
        ret = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                for rest in self.palPart(s[i:]):
                    ret.append([s[:i]] + rest)
        if not ret:
            return [[]]
        return ret


if __name__ == "__main__":
    print(Solution().palPart("aab"))
