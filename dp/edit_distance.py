"""
prob: n computer science, edit distance is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other.

There are three operations permitted on a word: replace, delete, insert. For example, the edit distance between "a" and "b" is 1, the edit distance between "abc" and "def" is 3
idea:
comp:
"""


def edit_distance(w1, w2):
    distance = [[i] for i in range(len(w1) + 1)]
    distance[0] = [j for j in range(len(w2) + 1)]
    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            insert = distance[i][j - 1] + 1
            delete = distance[i - 1][j] + 1
            replace = distance[i - 1][j - 1]
            if w1[i - 1] != w2[j - 1]:
                replace += 1
            distance[i].append(min(insert, delete, replace))
    return distance[-1][-1]


expected = 1
actual = edit_distance("a", "b")
print(expected == actual)

expected = 3
actual = edit_distance("abc", "def")
print(expected == actual)
