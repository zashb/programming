import itertools


def ltrCombPhnNum(s):
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    s_l = list(s)
    s_l_d = [d[i] for i in s_l]
    r = []
    for lp in range(len(s_l_d) - 1):
        for rp in range(lp + 1, len(s_l_d)):
            r.append(list(itertools.product(s_l_d[lp], s_l_d[rp])))
    return r


print(ltrCombPhnNum("23"))
