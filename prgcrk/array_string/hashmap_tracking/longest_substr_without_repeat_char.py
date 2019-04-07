"""
prob: Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
idea:
comp:
"""


def lswrc(string):
    string = list(string)
    n = len(string)
    if not string or n == 0:
        return 0
    res, i, Set = 1, 0, set()
    for j in range(n):
        if string[j] not in Set:
            Set.add(string[j])
            res = max(res, len(Set))
        else:
            while i < j:
                if string[i] == string[j]:
                    i += 1
                    break
                Set.remove(string[i])
                i += 1
    return res


expected = 3
actual = lswrc("abcabcbb")
print(expected == actual)
