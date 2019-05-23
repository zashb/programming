from collections import deque

def mergeSort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    else:
        midIdx = len(nums)//2
        a,b = mergeSort(nums[:midIdx]), mergeSort(nums[midIdx:])
        return merge(deque(a),deque(b))
def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a.popleft())
        else:
            c.append(b.popleft())
    if len(a) == 0:
        c += b
    if len(b) == 0:
        c += a
    return c
    

if __name__ == "__main__":
    print(mergeSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))