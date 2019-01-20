def grpAnag(w):
    d = {}
    for i in w:
        t = tuple(sorted(i))
        if t not in d:
            d[t] = [i]
        else:
            d[t].append(i)
    return d.values()


print(grpAnag(["eat", "tea", "tan", "ate", "nat", "bat"]))
