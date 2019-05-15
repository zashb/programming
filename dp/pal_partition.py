def pal_part(s):
    if not s:
        return s
    res = []
    if len(s) <= 1:
        res.append(s)
        return res

    table = [[float('-inf') for j in range(len(s))] for i in range(len(s))]

    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            k = i + j - 1
            if s[j] == s[k]:
                if i == 1 or i == 2:
                    table[j][k] = 1
                else:
                    table[j][k] = table[j + 1][k - 1]
                if table[j][k] == 1:
                    res.append(s[j:k + 1])
            else:
                table[j][k] = 0
    return res


# expected = ['a', 'a', 'b', 'aa']
# actual = pal_part('aab')
# print(expected == actual)
#
# expected = ['n', 'i', 't', 'i', 'n', 'iti', 'nitin']
# actual = pal_part('nitin')
# print(expected == actual)



# dfs
# def palPart(s):
#     ret = []
#     for i in range(1, len(s) + 1):
#         if s[:i] == s[i - 1::-1]:
#             for rest in palPart(s[i:]):
#                 ret.append([s[:i]] + rest)
#     if not ret:
#         return [[]]
#     return ret
#
#
# # expected = [['a', 'a', 'b'], ['aa', 'b']]
# # actual = palPart("aab")
# # print(expected == actual)
#
# # expected = [['n', 'i', 't', 'i', 'n'], ['n', 'iti', 'n'], ['nitin']]
# # actual = palPart('nitin')
# # print(expected == actual)
