class Int:
    def __init__(self, s, e):
        self.s,self.e = s,e

    def __repr__(self):
        return "[{},{}]".format(self.s, self.e)

def mergeInts(ints):
    ints_sort = sorted(ints, key=lambda x: x.s)
    res = []
    s, e = ints_sort[0].s, ints_sort[0].e
    for i in ints_sort:
        if i.s <= e:    e = max(e, i.e)
        else:
            res.append(Int(s, e))
            s,e = i.s,i.e
    res.append(Int(s, e))
    return res

if __name__ == '__main__':
    print(mergeInts([Int(1, 3), Int(2, 6), Int(8, 10), Int(15, 18)]))