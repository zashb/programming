class Solution:
    def palPairs(self, words):
        # res = []
        # lp, rp = 0, 1
        # while lp < len(words):
        #     while rp < len(words):
        #         concWords = words[lp] + words[rp]
        #         if concWords == concWords[::-1] and lp != rp:
        #             res.append([lp, rp])
        #         rp += 1
        #     lp += 1
        #     rp = 0
        #
        # return res

        res = []
        for lp in range(len(words)):
            for rp in range(lp + 1, len(words)):
                concWord = words[lp] + words[rp]
                concWord2 = words[rp] + words[lp]
                if concWord == concWord[::-1]  and lp != rp:
                    res.append([lp, rp])
                if concWord2 == concWord2[::-1] and lp!=rp:
                    res.append([rp,lp])
        return res


if __name__ == "__main__":
    print(Solution().palPairs(["bat", "tab", "cat"]))
    print(Solution().palPairs(["abcd", "dcba", "lls", "s", "sssll"]))
