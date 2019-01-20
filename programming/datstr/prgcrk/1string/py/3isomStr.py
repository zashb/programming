# def isomStr(s, t):
#     d_s, d_t = {}, {}
#     for i, j in enumerate(s):
#         if j not in d_s:
#             d_s[j] = [i]
#         else:
#             d_s[j].append(i)
#     for i, j in enumerate(t):
#         if j not in d_t:
#             d_t[j] = [i]
#         else:
#             d_t[j].append(i)
#     print(d_s, d_t)
#

def isomStr(s, t):
    # if not s or not t or len(s)!=len(t):    return False
    # map = {}
    # for i in range(len(s)):
    #     if s[i] in map:
    #         if map[s[i]]!=t[i]: return False
    #     elif t[i] in map:    return False
    #     map[s[i]] = t[i]
    # return True
    
    return list(map(s.find,s)) == list(map(t.index,t))

if __name__ == '__main__':
    print(isomStr("egg", "add"))
    print(isomStr("egg","fig"))

# algo
# map[a[idx]]==b[idx]