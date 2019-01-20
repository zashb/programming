import collections

def main(strs):
    d = collections.defaultdict(list)
    for s in strs:  d[tuple(sorted(s))].append(s)
    res = [i for i in d.values() if len(i) > 1]
    return res

if __name__ == '__main__':
    print(main(["eat", "tea", "tan", "ate", "nat", "bat"]))