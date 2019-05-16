"""
prob: find longest abs file path
idea: stack
comp:
ex:
"""


def longest_file_path(string):
    dict = {}
    longest = 0
    fileList = string.split("\n")
    for i in fileList:
        if "." not in i:  # 是文件夹
            key = i.count("\t")  # 是几级文件夹
            value = len(i.replace("\t", ""))  # 除去\t后的长度，是实际长度
            dict[key] = value
        else:  # 是文件。
            key = i.count("\t")
            # 　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
            length = sum([dict[j] for j in dict.keys() if j < key]) + len(i.replace("\t", "")) + key
            longest = max(longest, length)
    return longest


print(longest_file_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
