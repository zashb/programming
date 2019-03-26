def getMedian(nums1, nums2):
    j = 0
    med1, med2 = -1, -1
    for i in range(len(nums1) + 1):
        # if all elems of nums1<nums2
        if i == len(nums1):
            med1 = med2
            med2 = nums2[0]
            break
        # sly if nums2<nums1
        if j == len(nums1):
            med1 = med2
            med2 = nums1[0]
            break
        # store the prev median
        if nums1[i] < nums2[j]:
            med1 = med2
            med2 = nums1[i]
            i += 1
        # store the prev median
        else:
            med1 = med2
            med2 = nums2[j]
            j += 1
    return (med1 + med2) / 2


if __name__ == "__main__":
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45]
    if len(nums1) == len(nums2):
        print(getMedian(nums1, nums2))

# TTR:
# always med2 is copied to med1 and med2 is updated
# if nums1[i]<nums2[j],med1=med2,med2=nums1[i],i+=1
# else, med1=med2,med2=nums2[j],j+=1
