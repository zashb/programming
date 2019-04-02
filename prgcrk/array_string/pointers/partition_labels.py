"""
prob: A string string of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

For example:
Input: string = "ababfeefhijkh"
Output: [4,4,5]

Explanation:
The partition is "abab", "feef", "hijkh". This is a partition so that each letter appears in at most one part.

Idea: We need an array last[char] -> index of S where char occurs last. Then, let anchor and j be the start and end of the current partition. If we are at a label that occurs last at some index after j, we'll extend the partition j = last[c]. If we are at the end of the partition (i == j) then we'll append a partition size to our answer, and set the start of our new partition to i+1
Comp:
"""


def partition_labels(string):
    last = {c: i for i, c in enumerate(string)}
    right, left, res = 0, 0, []
    for i, c in enumerate(string):
        right = max(right, last[c])
        if i == right:
            res.append(i - left + 1)
            left = i + 1
    return res


string = "ababfeefhijkh"
expected = [4, 4, 5]
actual = partition_labels(string)
print(expected == actual)

string = "ababcbacadefegdehijhklij"
expected = [9, 7, 8]
actual = partition_labels(string)
print(expected == actual)
