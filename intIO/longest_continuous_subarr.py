"""
return len of longest contin subarr
Idea : if prev elem in lookup : continue, else: start a streak
comp : O(n^2)
"""


def longest_contin_subarr(arr):
    if arr is None:
        return 0
    lookup = set(arr)
    res = 0
    for i in arr:
        if i - 1 in lookup:
            continue
        streak = 1
        while i + streak in lookup:
            streak += 1
            res = max(res, streak)
    return res


# def longest_contin_subarr(arr):
#     n = len(arr)
#     if not arr or n == 0:
#         return arr
#     Set, Max = set(), 1
#     for i in arr:
#         Set.add(i)
#     for i in arr:
#         l, r, count = i - 1, i + 1, 1
#         while l in Set:
#             count += 1
#             Set.remove(l)
#             l -= 1
#         while r in Set:
#             count += 1
#             Set.remove(r)
#             r += 1
#         Max = max(Max, count)
#     return Max


# def longest_contin_subarr(arr):
#     lookup = set(arr)
#     res = 0
#     for i in arr:
#         if i - 1 not in lookup:
#             j = i
#             while j in lookup:
#                 j += 1
#             res = max(res, j - i)
#     return res


arr = [1, 9, 3, 10, 4, 20, 2]
expected = 4
actual = longest_contin_subarr(arr)
print(expected == actual)

arr = [5, 2, 99, 3, 4, 100, 1, 49, 5]
expected = 5
actual = longest_contin_subarr(arr)
print(expected == actual)

arr = [100, 4, 200, 1, 3, 2]
expected = 4
actual = longest_contin_subarr(arr)
print(expected == actual)

arr = [100, 4, 200, 1, 3, 2, 5, 6, 201, 202, 203, 204, 205]
expected = 6
actual = longest_contin_subarr(arr)
print(expected == actual)
