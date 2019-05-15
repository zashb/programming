"""
prob: www.test.com/1/2/3/4/./5/6/7/8/../3
output: www.test.com/1/2/3/5/6/3
idea: stack
comp: O(n)
"""


def dot_compressor(url):
    if not url:
        return ""
    split = url.split("/")
    string_stack = [split[0]]
    for i in range(1, len(split)):
        if split[i].isalnum():
            string_stack.append(split[i])
        else:
            dot_count = split[i].count(".")
            while dot_count > 0:
                string_stack.pop()
                dot_count -= 1
    return "/".join(string_stack)


expected = "www.test.com/1/2/3/5/6/3"
actual = dot_compressor("www.test.com/1/2/3/4/./5/6/7/8/../3")
print(expected == actual)

expected = ""
actual = dot_compressor("")
print(expected == actual)

expected = "www.test.com/1/2/3/3"
actual = dot_compressor("www.test.com/1/2/3/4/./5/6/../7/8/../3")
print(expected == actual)

expected = ""
actual = dot_compressor("./5/6/../7/8/../3")
print(expected == actual)
