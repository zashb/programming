class Solution:
    def intrscn1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intrscn2(self, nums1, nums2):
        # return [i for i in min([nums1,nums2],key=lambda x:len(x)) if i in max([nums1,nums2],key=lambda x:len(x))]

        # make a list of both the lists
        numsList = [nums1] + [nums2]
        # sort them by len
        numsList = sorted(numsList, key=lambda x: len(x))
        # for each elem in smaller list, if it is in the larger list return
        return [i for i in numsList[0] if i in numsList[1]]


if __name__ == "__main__":
    print(Solution().intrscn1([1, 2, 2, 1], [2, 2]))
    print(Solution().intrscn2([1, 2, 2, 1], [2, 2]))
