# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true

import collections


class Solution:
    def fun(self, s1, s2):
        d1, d2 = collections.defaultdict(list), collections.defaultdict(list)
        for idx, char in enumerate(s1):
            d1[char].append(idx)
        # print(d1)
        for idx, char in enumerate(s2):
            d2[char].append(idx)
        # print(d2)
        print(d1.values(),"\n",d2.values())
        return sorted(d1.values()) == sorted(d2.values())


if __name__ == "__main__":
    print(Solution().fun("egg", "add"))
    print(Solution().fun("eggg", "add"))
    print(Solution().fun("foo", "bar"))

    # TTR:
    # check if len of sets and len of set of zip are equal
