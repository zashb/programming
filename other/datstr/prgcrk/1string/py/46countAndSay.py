import itertools

def main(n):
    s = '1'
    for _ in range(n - 1):
        cntOfDig = []
        for key, grp in itertools.groupby(s):   cntOfDig.append(str(len(list(grp))) + str(key))
        s = "".join(cntOfDig)
    return s


if __name__ == "__main__":
    print(main(1))
    print(main(4))
