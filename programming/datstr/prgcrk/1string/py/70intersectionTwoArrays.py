import collections

def main1(nums1,nums2):
    return list(set(nums1)&set(nums2))

def main2(nums1,nums2):
    a,b=map(collections.Counter,(nums1,nums2))
    return list((a&b).elements())

if __name__ == '__main__':
    print(main1(nums1 = [1, 2, 2, 1], nums2 = [2, 2]))
    print(main2(nums1 = [1, 2, 2, 1], nums2 = [2, 2]))