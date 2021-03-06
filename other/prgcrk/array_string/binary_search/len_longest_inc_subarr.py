"""
prob: Given an unsorted array of integers, find the length of longest increasing subsequence.
For example, given [10, 9, 2, 5, 3, 7, 101, 18], the longest increasing subsequence is [2, 3, 7, 101]. Therefore the length is 4
idea:
for each num in nums
     if(list.size()==0)
          add num to list
     else if(num > last element in list)
          add num to list
     else
          replace the element in the list which is the smallest but bigger than num
comp: O(n logn)
"""


def len_lis(arr):
    if not arr or len(arr) == 0:
        return -1
    res = []
    for i in arr:
        if len(res) == 0 or i > res[-1]:
            res.append(i)
        else:
            l, r = 0, len(res) - 1
            while l < r:
                mid = (l + r) // 2
                if i > res[mid]:
                    l = mid + 1
                else:
                    r = mid
            res[r] = i
    return len(res)


expected = 4
actual = len_lis([10, 9, 2, 5, 3, 7, 101, 18])
print(expected == actual)
