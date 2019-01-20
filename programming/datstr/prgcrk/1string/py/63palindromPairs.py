def main(words):
    wordict,res = {},[]
    for i in range(len(words)): wordict[words[i]] = i
    for i in range(len(words)):
        for j in range(len(words[i])+1):
            tmp1,tmp2 = words[i][:j],words[i][j:]
            if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]: res.append([i,wordict[tmp1[::-1]]])
            if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:    res.append([wordict[tmp2[::-1]],i])
    return res

if __name__ == '__main__':
    print(main(words = ["bat", "tab", "cat"]))
    print(main(words = ["abcd", "dcba", "lls", "s", "sssll"]))