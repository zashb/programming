"""
reverse string
Idea : append each char to i + ""
comp : O(n)
"""


# def reverse_string(string):
#     res = ""
#     for char in string:
#         res = char + res
#     return res

def reverse_string(string):
    string, lp, rp = list(string), 0, len(string) - 1
    while lp < rp:
        string[lp], string[rp] = string[rp], string[lp]
        lp += 1
        rp -= 1
    return "".join(string)


string = "hello"
expected = "olleh"
actual = reverse_string(string)
print(expected == actual)
