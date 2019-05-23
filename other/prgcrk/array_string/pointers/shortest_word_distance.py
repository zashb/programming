"""
prob: Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.
idea: 2 ptrs, update idx if ==, compute min only if == -1
comp:
"""


def shortest_word_distance(words, w1, w2):
    m, n, Min = -1, -1, float('inf')
    for i in range(len(words)):
        if w1 == words[i]:
            m = i
            if n != -1:
                Min = min(Min, m - n)
        elif w2 == words[i]:
            n = i
            if m != -1:
                Min = min(Min, n - m)
    return Min


expected = 3
actual = shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
print(expected == actual)

expected = 1
actual = shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes")
print(expected == actual)
