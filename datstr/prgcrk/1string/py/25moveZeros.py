def moveZeros(nums):
	if not nums or len(nums)==0:	return
	insertPos=0
	for i in nums:
		if i!=0:
			nums[insertPos]=i
			insertPos+=1
	while insertPos<len(nums):
		nums[insertPos]=0
		insertPos+=1
	return nums

if __name__=="__main__":
	print(moveZeros([0,-1,0,3,12]))