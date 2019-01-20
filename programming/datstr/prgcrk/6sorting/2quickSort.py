def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList
def partition(myList, start, end):
    pivot,left,right = myList[start],start+1,end
    done = False
    while not done:
        # if pivot >= left elem, inc left idx
        while right >= left and pivot >= myList[left]:
            left += 1
        # if pivot <= right elem, dec right idx
        while right >= left and pivot <= myList[right]:
            right -= 1
        if right < left:
            done= True
        else:
            # swap places
            myList[left],myList[right] = myList[right],myList[left]
    # swap start with myList[right]
    myList[start],myList[right] = myList[right],myList[start]
    return right


if __name__ == '__main__':
    nums = [54,26,93,17,77,31,44,55,20]
    print(quicksort(nums,0,len(nums)-1))