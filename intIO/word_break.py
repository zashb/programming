"""
check if a string can be segmented into space-seperated sequence of 1 or more dictionary words
Idea : dp, bool arr, forw ptr, backw ptr, lookup [rp:fp] return [-1]
comp : O(n^2)
"""


def word_break(string, lookup):
    n = len(string)
    word_check = [False] * (n + 1)
    word_check[0] = True
    for fp in range(1, n + 1):
        for bp in range(fp - 1, -1, -1):
            if word_check[fp] == True:
                break
            if word_check[bp] == True:
                if string[bp:fp] in lookup:
                    word_check[fp] = True
    return word_check[-1]


string = "applepenapple"
# lookup = {"apple", "pen"}
lookup = {"appl", "pen", "e"}
expected = True
actual = word_break(string, lookup)
print(expected == actual)

string = "routingnumber"
lookup = {"rout", "ing", "number"}
expected = True
actual = word_break(string, lookup)
print(expected == actual)
