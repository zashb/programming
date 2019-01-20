# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k

def contDups_2(n,k):
	dic = {}
	for i,j in enumerate(n):
		if j in dic and i-dic[j] <= k:	return True
		dic[j] = i      
	return False

if __name__=="__main__":
	print(contDups_2([1,2,3,3,3,3,3,3,3,1,123,123,231,2,3,1,2,245636745,74,567,45667,567,4567,56,7,6,6,6,7,7],2))
	print(contDups_2([1,2,3,13,23,3],2))