"""
prob: find longest abs file path
idea: stack/dict, track stack len with dict
comp:
ex:
"""


def longest_file_path(string):
    maxlen = 0
    pathlen = {0: 0}
    for line in string.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen

    # dict = {}
    # longest = 0
    # fileList = string.split("\n")
    # for i in fileList:
    #     if "." not in i:
    #         key = i.count("\t")
    #         value = len(i.replace("\t", ""))
    #         dict[key] = value
    #     else:
    #         key = i.count("\t")
    #         length = sum([dict[j] for j in dict.keys() if j < key]) + len(i.replace("\t", "")) + key
    #         longest = max(longest, length)
    # return longest


expected = 20
actual = longest_file_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print(expected == actual)
