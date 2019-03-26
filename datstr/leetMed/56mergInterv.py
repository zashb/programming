class Int:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __repr__(self):
        return "[{},{}]".format(self.s, self.e)


def mergInterv(Ints):
    if len(Ints) <= 1:
        return Ints
    ints_sort = sorted(Ints, key=lambda x: x.s)
    res = []
    s, e = ints_sort[0].s, ints_sort[0].e
    for i in ints_sort:
        if i.s <= e:
            e = max(e, i.e)
        else:
            res.append(Int(s, e))
            s = i.s
            e = i.e
    res.append(Int(s, e))
    return res


if __name__ == '__main__':
    print(mergInterv([Int(1, 3), Int(2, 6), Int(8, 10), Int(15, 18)]))

