import collections


class Solution:
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            # since list can have dups and keys cant repeat,thus it is converted to tuple, which is allowed as key
            d[tuple(sorted(s))].append(s)
        # print(d)
        res = [i for i in d.values() if len(i) > 1]
        return res
        # return [j for i in res for j in i]


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", "hutt", "tuth"]))

# TTR:
# create a dict with alphabet-set as keys and elems as vals - d[tuple(sorted(s))].append(s)
# use sorting to club similar indices
