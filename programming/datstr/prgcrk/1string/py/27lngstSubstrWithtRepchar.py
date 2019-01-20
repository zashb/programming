def lngstSubstrWithtRepchar(s):
	res,res_i=[[]],0
	for i in s:
		if i not in res[res_i]:	res[res_i].append(i)
		else:
			res.append([])
			res_i+=1
			res[res_i].append(i)
	# print(res) 
	return len(max(res,key=lambda x:len(x)))

if __name__=="__main__":
	print(lngstSubstrWithtRepchar("abcabcbb"))
	print(lngstSubstrWithtRepchar("bbbb"))

# algo
# res is a list of subseq with non-rep char