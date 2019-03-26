def grpAnag(w):
    d = {}
    for i in w:
        # key of dic must be immutable
        t = tuple(sorted(i))
        d.setdefault(t, [i]).append(i)
        # if t not in d:
        #     d[t] = [i]
        # else:
        #     d[t].append(i)
    return d.values()


print(grpAnag(["eat", "tea", "tan", "ate", "nat", "bat"]))
