def mergeSortedArrs(a, b):
    a, b = sorted(a), sorted(b)
    m,n = len(a),len(b)
    if m>n: a+=[0]*n
    if n>m: b+=[0]*m
    while m > 0 and n > 0:
        if a[m - 1] > b[n - 1]:
            a[m + n - 1] = a[m - 1]
            m -= 1
        else:
            a[m + n - 1] = b[n - 1]
            n -= 1
    while n > 0:
        a[m + n - 1] = b[n - 1]
        n -= 1
    return a

if __name__ == '__main__':
    print(mergeSortedArrs([3, 4, 4, 5, 5, 6, 7], [5, 4, 3, 2, 2, 1]))

# algo
# compare elems from end
# while m>0 and n>0: if a[m-1]>b[n-1]: a[m+n-1]=a[m-1] m-=1 else b n-=1]