#  find the length of the longest consecutive elements sequence

def lngstConsecSeq(n):

	# n_s = sorted(n)
	# res = []
	# for i,j in enumerate(n_s):
	# 	if j+1 in n_s or j-1 in res:
	# 		res.append(j)
	# return len(res)

	res,map = 0,{}
	for i in n:
		if i not in map:
			left = map[i-1] if i-1 in map else 0
			right = map[i+1] if i+1 in map else 0
			_sum = left+right+1
			map[i]=map[i-left]=map[i+right] = _sum
			res = max(res,_sum)
		else:	continue
	return res

if __name__ == '__main__':
	print(lngstConsecSeq([100, 4, 200, 1, 3, 2]))

# algo
# number_seqlen_map={},max_seqlen=0
# if new elem: l=map[i-1],sly r, sum=l+r+1, map[i]=map[i-1]=map[i+1]=sum
# else: continue