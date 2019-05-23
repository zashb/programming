"""
prob: Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
idea:
comp:
"""


# def lswrc(string):
#     string = list(string)
#     n = len(string)
#     if not string or n == 0:
#         return 0
#     res, i, Set = 1, 0, set()
#     for j in range(n):
#         if string[j] not in Set:
#             Set.add(string[j])
#             res = max(res, len(Set))
#         else:
#             while i < j:
#                 if string[i] == string[j]:
#                     i += 1
#                     break
#                 Set.remove(string[i])
#                 i += 1
#     return res


# def lswrc(string):
#     n, max_len, curr_len, prev_idx, i = len(string), 1, 1, 0, 0
#     visited = [-1] * 128
#     visited[ord(string[0])] = 0
#     for i in range(1, n):
#         prev_idx = visited[ord(string[i])]
#         if i - prev_idx > curr_len:
#             curr_len += 1
#         else:
#             if curr_len > max_len:
#                 max_len = curr_len
#             curr_len = i - prev_idx
#         visited[ord(string[i])] = i
#     if curr_len > max_len:
#         max_len = curr_len
#     return max_len


def lswrc(s):
    res, res_i = [[]], 0
    for i in s:
        if i not in res[res_i]:
            res[res_i].append(i)
        else:
            res.append([i])
            res_i += 1
    return len(max(res, key=len))


expected = 3
actual = lswrc("abcabcbb")
print(expected == actual)

expected = 1
actual = lswrc("bbbb")
print(expected == actual)
