"""
Idea : BT
Com : O(n*n!)
"""

# def all_perm(nums):
#     ans = [[]]
#     for n in nums:
#         new_ans = []
#         for l in ans:
#             for i in range(len(l) + 1):
#                 new_ans.append(l[:i] + [n] + l[i:])
#                 if i < len(l) and l[i] == n:
#                     break  # handles duplication
#         ans = new_ans
#     return ans

from collections import Counter


def all_perm(nums):
    def btrack(ans, path, counter):
        if len(path) == len(nums):
            ans.append(path[:])
        for x in counter:  # dont pick duplicates
            if counter[x] > 0:
                path.append(x)
                counter[x] -= 1
                btrack(ans, path, counter)
                path.pop()
                counter[x] += 1

    ans, temp = [],[]
    btrack(ans, temp, Counter(nums))
    return ans


expected = [[3, 1, 2], [1, 3, 2], [1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
actual = all_perm([2, 1, 3])
print(expected == actual)

expected = [[1, 3, 2, 1], [3, 1, 2, 1], [3, 2, 1, 1], [1, 2, 3, 1], [2, 1, 3, 1], [2, 3, 1, 1], [1, 2, 1, 3],
            [2, 1, 1, 3], [1, 3, 1, 2], [3, 1, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]
actual = all_perm([1, 2, 3, 1])
print(expected == actual)

expected = [['c', 'b', 'a'], ['b', 'c', 'a'], ['b', 'a', 'c'], ['c', 'a', 'b'], ['a', 'c', 'b'], ['a', 'b', 'c']]
actual = all_perm(list("abc"))
print(expected == actual)
