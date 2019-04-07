"""
prob: Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. For example, given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
idea: queue of curr_word, curr_len
comp:
"""
from collections import deque


def word_ladder(start, end, word_list):
    # set of words to traverse
    word_set = set()
    for word in word_list:
        word_set.add(word)
    # since all words are the same len, we dont update the len later
    word_len = len(start)
    queue = deque([(start, 1)])
    while queue:
        curr_word, curr_len = queue.popleft()
        if curr_word == end:
            return curr_len
        else:
            for i in range(word_len):
                part1 = curr_word[:i]
                part2 = curr_word[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curr_word[i] != j:
                        next_word = part1 + j + part2
                        if next_word in word_set:
                            queue.append((next_word, curr_len + 1))
                            word_set.remove(next_word)
    return 0


expected = 5
actual = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(expected == actual)
