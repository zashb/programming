import collections


# find the minimum window in s which will contain all the characters in t
def minWinSubstr(string, substring):
    substring_counter, n_substring = collections.Counter(substring), len(substring)
    i, I, J = 0, 0, 0
    for j in range(len(string)):
        if substring_counter[string[j]] > 0:
            n_substring = n_substring - substring_counter[string[j]]
        substring_counter[string[j]] = substring_counter[string[j]] - 1
        if n_substring == 0:
            while i < j and substring_counter[string[i]] < 0:
                substring_counter[string[i]] = substring_counter[string[i]] + 1
                i += 1
            if J == 0 or j - i <= J - I:
                I, J = i, j
    return string[I:J + 1]


if __name__ == "__main__":
    string = "ADOBECODEBANC"
    substring = "ABC"
    expected = "BANC"
    actual = minWinSubstr(string, substring)
    print(actual == expected)

    string = "geeksforgeeks"
    substring = "ork"
    expected = "ksfor"
    actual = minWinSubstr(string, substring)
    print(expected == actual)
