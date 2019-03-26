class Solution:
    def shortestPal(self, s):
        # lp, rp = 0, 1
        # palList = []
        # while rp < len(s):
        #     buildPal = s[rp:][::-1] + s[lp:]
        #     if buildPal == buildPal[::-1] and len(buildPal):
        #         palList.append(buildPal)
        #     rp += 1
        # # print(palList)
        # return min(palList, key=lambda x: len(x))

        for rp in range(1, len(s) + 1):
            wrd = s[1:rp][::-1] + s
            if wrd == wrd[::-1]:
                print(wrd)
                print(len(wrd))
                break


if __name__ == "__main__":
    print(Solution().shortestPal("aacecaaa"))
    print(Solution().shortestPal("abcd"))
