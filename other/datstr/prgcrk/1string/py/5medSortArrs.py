# return median of 2 sorted arrays

def main(n1, n2):
    tot_len = len(n1) + len(n2)
    if tot_len % 2 == 0:    return (findMedian(tot_len // 2, n1, n2, 0, 0)+findMedian(tot_len // 2 + 1, n1, n2, 0, 0)) / 2
    else:   return findMedian((tot_len+1)//2, n1, n2, 0, 0)

def findMedian(m, n1, n2, s1, s2):
    if s1 >= len(n1):   return n2[s2 + m - 1]
    if s2 >= len(n2):   return n1[s1 + m - 1]
    if m == 1:  return min(n1[s1], n2[s2])
    m1, m2 = s1 + m // 2 - 1, s2 + m // 2 - 1
    mid1, mid2 = n1[m1] if m1 < len(n1) else 99999, n2[m2] if m2 < len(n2) else 99999
    if (mid1 < mid2):   return findMedian(m - m // 2, n1, n2, m1 + 1, s2)
    else:   return findMedian(m - m // 2, n1, n2, s1, m2 + 1)

# def main(a,b):
#     m,n=len(a),len(b)
#     if m>n: a,b,m,n=b,a,n,m
#     if n==0: raise ValueError
#     imin,imax,half_len=0,m,(m+n+1)//2
#     while imin<=imax:
#         i=(imin+imax)//2
#         j=half_len-i
#         if i<m and b[j-1]>a[i]: imin=i+1
#         elif i>0 and a[i-1]>b[j]:   imax=i-1
#         else:
#             if i==0:    max_of_left=b[j-1]
#             elif j==0:  max_of_left=a[i-1]
#             else:   max_of_left=max(a[i-1],b[j-1])
#             if (m+n)%2==1:  return max_of_left
#             if i==m:    min_of_right=b[j]
#             elif j==n:  min_of_right=a[i]
#             else:   min_of_right=min(a[i],b[j])
#             return (max_of_left+min_of_right)/2.0

if __name__ == '__main__':
    print(main([1,3],[2]))
    print(main([1,2],[3,4]))

# algo
# recursive, 2 funcs
# if totlen is even then avg(//2+1,//2) else //2+1
# m1 = s1+k//2-1,sly m2,s2
# mid1=n1[m1], sly mid2,m2
# if mid2>mid1 recurse(k-k//2,s1=m1+1) else recurse(k-k//2,s2=m2+1)