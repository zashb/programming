def srchRng(n, v):
    # n = sorted(n)
    # i, j = 0, len(n) - 1
    # res = []
    # while i < j:
    #     m = (i + j) // 2
    #     if n[m] < v:
    #         i = m + 1
    #     else:
    #         j = m
    # if n[i] != v:
    #     return res
    # else:
    #     res.append(i)
    # i,j = 0, len(n) - 1
    # while i < j:
    #     m = (i + j) // 2 + 1
    #     if n[m] > v:
    #         j = m - 1
    #     else:
    #         i = m
    # res.append(j)
    # return res

    def srch(t):
        lo, hi = 0, len(n)
        while lo < hi:
            mid = (lo + hi) // 2
            if n[mid] >= t:
                hi = mid
            else:
                lo = mid + 1
        return lo

    lo = srch(v)
    # if v in n[lo:lo + 1]:
    if v == n[lo]:
        return [lo, srch(v + 1) - 1]
    else:
        return [-1, -1]


if __name__ == '__main__':
    print(srchRng([5, 7, 7, 8, 8, 8, 10], 8))
