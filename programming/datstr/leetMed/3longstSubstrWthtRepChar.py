from timeit import default_timer as timer


class Solution:
    def longstSubstrWthtRepChar(self, s):
        # lp, lens = 0, []
        # for rp in range(lp + 1, len(s)):
        #     if s[rp] not in s[lp:rp]:
        #         continue
        #     else:
        #         lens.append(len(s[lp:rp]))
        #         lp = rp
        # return max(lens)

        if len(s) == 0:
            return 0
        d, m, j = {}, 0, 0
        for i in range(len(s)):
            print(i)
            if s[i] in d:
                j = max(j, d[s[i]] + 1)
            d[s[i]] = i
            m = max(m, i - j + 1)
            print(d,"\t",m,"\t",j)
        return m


if __name__ == "__main__":
    s = Solution()
    # a = timer()
    # print(s.longstSubstrWthtRepChar("abcabcbb"))
    # b = timer()
    # print(round(b-a,ndigits=4))
    print(s.longstSubstrWthtRepChar("abcabcbb"))
