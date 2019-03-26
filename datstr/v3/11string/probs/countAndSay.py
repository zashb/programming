import itertools


class Solution:
    def countAndSay(self, n):
        s = '1'
        # for _ in range(n - 1):
        #     cntOfDigit = (str(len(list(group))) + str(digit) for digit, group in itertools.groupby(s))
        #     s = "".join(cntOfDigit)
        # return s

        for _ in range(n - 1):
            cntOfDig = []
            for key, grp in itertools.groupby(s):
                cntOfDig.append(str(len(list(grp))) + str(key))
            s = "".join(cntOfDig)
        return s


if __name__ == "__main__":
    for i in range(1, 5):
        print(Solution().countAndSay(i))

        # TTR:
        # itertools.groupby
        # rem the whole damn procedure
