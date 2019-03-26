def lngstSubstrWithAtmostKDistChar(s,k):
	dic,low,res = {},0,0
	for i,j in enumerate(s):
		dic[j] = i
		if k < len(dic):
			low = min(dic.values())
			del dic[s[low]]
			low += 1
		res = max(res, i-low+1)
	return res

if __name__ == "__main__":
	print(lngstSubstrWithAtmostKDistChar("aabacbebebe",3))

# algo
# dic of j:i,low,res
# if k < len(d) "atmost  k":update l,del from dic,inc it