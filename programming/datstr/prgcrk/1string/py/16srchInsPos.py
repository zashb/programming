def srchInsPos(n,t):
	# n_s = sorted(n)
	# if t < n_s[0]:
	# 	# n_s = [t] + n_s
	# 	return 0
	# if t > n_s[-1]:
	# 	# n_s += [t]
	# 	return len(n_s)
	# i,j = 0,len(n)
	# while i<j:
	# 	mid = (i+j)//2
	# 	if t>n[mid]:
	# 		i=mid+1
	# 	else:
	# 		j=mid
	# return i # can return i or j

	return len([i for i in n if i<t])

if __name__ == '__main__':
	print(srchInsPos([1,3,5,6],0))
	print(srchInsPos([1,3,5,6],7))
	print(srchInsPos([1,3,5,6],5))
	print(srchInsPos([1,3,5,6],2))

# algo
# i,j=0,len
# while i<j: m=(i+j)//2, compare with t and inc/dec i/j 
# return j