# import itertools
# class Solution:
# 	def threeSumClosest(self,nums,target):
# 		combs=itertools.combinations(nums,3)
# 		sums=[sum(i) for i in combs]
# 		d = {i:abs(target-i) for i in sums}
# 		print(min(d,key=lambda x:d[x]))

# if __name__=="__main__":
# 	s = Solution()
# 	s.threeSumClosest([-1,2,1,-4],1)

# import collections
# class Solution:
# 	def bullsAndCows(self,n1,n2):
# 		n1Dict=collections.defaultdict(list)
# 		n2Dict=collections.defaultdict(list)
# 		for i,j in enumerate(n1):
# 			n1Dict[j].append(i)
# 		for i,j in enumerate(n2):
# 			n2Dict[j].append(i)	
# 		# print(n1Dict)
# 		# print(n2Dict)
# 		bc,cc=0,0
# 		for i in n2Dict:
# 			if i in n1Dict:
# 				for j in n1Dict[i]:
# 					if j in n2Dict[i]:
# 						bc+=1
# 					else:
# 						cc+=1
# 		print(str(bc)+"A"+str(cc)+"B")

# if __name__=="__main__":
# 	s = Solution()
# 	s.bullsAndCows("1807","7810")
# 	s.bullsAndCows("1123","0111")

# class Solution:
# 	def mostWater(self,heights):
# 		maxArea=0
# 		for lp in range(0,len(heights)-1):
# 			for rp in range(lp+1,len(heights)):
# 				maxArea=max(maxArea,min(heights[lp],heights[rp])*(rp-lp))
# 		print(maxArea)

# if __name__=="__main__":
# 	s=Solution()
# 	s.mostWater([1, 2, 3, 4, 3, 2, 1, 5])

# import itertools
# class Solution:
# 	def countAndSay(self,n):
# 		say="1"
# 		for _ in range(n-1):
# 			cnt=[]
# 			for key,grp in itertools.groupby(say):
# 				cnt.append(str(len(list(grp)))+str(key))
# 			say="".join(cnt)
# 		print(say)

# if __name__=="__main__":
# 	s=Solution()
# 	for i in range(1,5):
# 		s.countAndSay(i)

# import collections
# class Solution:
# 	def groupAnagrams(self,words):
# 		d=collections.defaultdict(list)
# 		for i in words:
# 			d[tuple(sorted(i))].append(i)
# 		print(list(d.values()))

# if __name__=="__main__":
# 	s=Solution()
# 	s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", "hutt", "tuth"])

# class Solution:
# 	def hIndex(self,nums):
# 		nums=sorted(nums)
# 		for i,j in enumerate(nums):
# 			if j==len(nums[i:]) and len(nums[:i])<j:
# 				print(j)
# 			else:
# 				continue

# if __name__=="__main__":
# 	s=Solution()
# 	s.hIndex([3,0,6,1,5])

# class Solution:
# 	def intersection1(self,n1,n2):
# 		print(set(n1)&set(n2))
# 		print([i for i in n2 if i in n1])

# if __name__=="__main__":
# 	s=Solution()
# 	s.intersection1([1, 2, 2, 1], [2, 2])

# import collections
# class Solution:
# 	def isIsom(self,s1,s2):
# 		s1D=collections.defaultdict(list)
# 		s2D=collections.defaultdict(list)
# 		for i,j in enumerate(s1):
# 			s1D[j].append(i)
# 		for i,j in enumerate(s2):
# 			s2D[j].append(i)
# 		print(sorted(s1D.values())==sorted(s2D.values()))

# if __name__=="__main__":
# 	s=Solution()
# 	s.isIsom("egg", "add")
# 	s.isIsom("eggg", "add")
# 	s.isIsom("foo", "bar")

# class Solution:
# 	def largestRectArea(self,hist):
# 		hist.append(0)
# 		maxArea,idxStack=0,[-1]
# 		for i,j in enumerate(hist):
# 			while j<hist[idxStack[-1]]:
# 				h=hist[idxStack.pop()]
# 				w=i-idxStack[-1]-1
# 				maxArea=max(maxArea,h*w)
# 			idxStack.append(i)
# 		print(maxArea)

# if __name__=="__main__":
# 	s=Solution()
# 	s.largestRectArea([6,2,5,4,5,1,6])

# class Solution:
# 	def lenLngstSubstr(self,s):
# 		lp,subStr=0,[]
# 		for rp in range(lp+1,len(s)):
# 			if s[rp] not in s[lp:rp]:
# 				continue
# 			else:
# 				subStr.append(s[lp:rp])
# 				lp=rp
# 		print(subStr)
# 		print(max(subStr,key=lambda x:len(x)))

# if __name__=="__main__":
# 	s=Solution()
# 	s.lenLngstSubstr("abcabcbb")
# 	s.lenLngstSubstr("bbbbb")
# 	s.lenLngstSubstr("pwwkew")

# class Interval:
# 	def __init__(self,s,e):
# 		self.start=s
# 		self.end=e
# 	def __repr__(self):
# 		return "[{},{}]".format(self.start,self.end)
# class Solution:
# 	def mergeIntevs(self,intervals):
# 		print(intervals)
# 		intervals=sorted(intervals,key=lambda x:x.start)
# 		res=[intervals[0]]
# 		for i,j in enumerate(intervals):
# 			prev=res[-1]
# 			if j.start <= prev.end:
# 				prev.end=max(prev.end,j.end)
# 			else:
# 				res.append(j)
# 		print(res)

# if __name__ == '__main__':
# 	s=Solution()
# 	s.mergeIntevs([Interval(1, 3), Interval(2, 6), Interval(15, 18), Interval(8, 10)])

# import itertools
# class Solution:
# 	def minSizeSubArrSum(self,nums,target):
# 		for i in range(len(nums)):
# 			combs=itertools.combinations(nums,i)
# 			sums=[sum(j) for j in combs];print(sums)
# 			if target in sums:
# 				print(i);break

# if __name__ == '__main__':
# 	s=Solution()
# 	s.minSizeSubArrSum([2,3,1,2,4,3],7)

# class Solution:
# 	def cntGrtr(self,nums):
# 		cnts=[]
# 		for lp in range(len(nums)):
# 			cnt=0
# 			for rp in range(lp+1,len(nums)):
# 				if nums[rp]>nums[lp]:
# 					cnt+=1 
# 			cnts.append(cnt)
# 		print(cnts)

# if __name__ == '__main__':
# 	s=Solution()
# 	s.cntGrtr([5,3,9,8,2,6])

# class Solution:
# 	def revVows(self,s):
# 		vows=[i for i in s if i in "aeiou"]
# 		res=[i if i not in "aeiou" else vows.pop() for i in s]
# 		print("".join(res))

# if __name__ == '__main__':
# 	s=Solution()
# 	s.revVows("hello")
# 	s.revVows("leetcode")

# class Solution:
# 	def revPolNot(self,s):
# 		stack=[]
# 		for i in s:
# 			if i in "+-/*":
# 				b,a=stack.pop(),stack.pop()
# 				i=repr(int(eval(a+i+b)))
# 			stack.append(i)
# 		print(stack)

# if __name__ == '__main__':
# 	s=Solution()
# 	s.revPolNot(["2", "1", "+", "3", "*"])
# 	s.revPolNot(["4", "13", "5", "/", "+"])

# class Solution:
# 	def searchRange(self,nums,target):
# 		res=[]
# 		for i,j in enumerate(nums):
# 			if j==target:
# 				for rp in range(i+1,len(nums)):
# 					if nums[rp]==target:
# 						continue
# 					else:
# 						res.append([i,rp-1])
# 						break
# 		print(res)

# if __name__ == '__main__':
# 	s=Solution()
# 	s.searchRange([5, 7, 7, 8, 8, 10], 8)
# 	s.searchRange([5, 7, 7, 8, 7,8, 10], 7)

# class Solution:
# 	def shortstPal(self,s):
# 		for rp in range(1,len(s)+1):
# 			wrd=s[1:rp][::-1]+s
# 			if wrd==wrd[::-1]:
# 				print(wrd)
# 				print(len(wrd))
# 				break

# if __name__ == '__main__':
# 	s=Solution()
# 	s.shortstPal("aacecaaa")
# 	s.shortstPal("abcd")

# class Solution:
# 	def slidWindMax(self,nums,windLen):
# 		res=[]
# 		for lp in range(len(nums)-2):
# 			wind=nums[lp:lp+windLen]
# 			wind_max=max(wind)
# 			res.append(wind_max)
# 		print(res)
# 	def slidWindMed(self,nums,windLen):
# 		res=[]
# 		for lp in range(len(nums)-2):
# 			wind=nums[lp:lp+windLen]
# 			wind_sorted=sorted(wind)
# 			med=wind_sorted[(len(wind_sorted)-1)//2]
# 			res.append(med)
# 		print(res)

# if __name__ == '__main__':
# 	s=Solution()
# 	s.slidWindMax([1, 3, -1, -3, 5, 3, 6, 7], 3)
# 	s.slidWindMed([1, 3, -1, -3, 5, 3, 6, 7], 3)

# class Solution:
# 	def summRange(self,nums):
# 		lp,stEndIdxDict=0,{}
# 		for rp in range(lp+1,len(nums)):
# 			if nums[lp:rp+1]==list(range(nums[lp],nums[rp]+1)):
# 				stEndIdxDict[lp]=rp
# 			else:
# 				lp=rp
# 		res=[]
# 		for k,v in stEndIdxDict.items():
# 			res.append("["+str(nums[k])+","+str(nums[v])+"]")
# 		res.append(str(nums[-1]))
# 		print(res)

# if __name__=="__main__":
# 	s=Solution()
# 	s.summRange([-3,-2,-1,0,1,2,4,5,7])

# class Solution:
# 	def trapRainWat(self,nums):
# 		n=len(nums)
# 		left,right,water=[0]*n,[0]*n,0
# 		left[0]=nums[0]
# 		for i in range(1,n):
# 			left[i]=max(left[i-1],nums[i])
# 		# print(left)
# 		right[n-1]=nums[n-1]
# 		for i in range(n-2,0,-1):
# 			right[i]=max(right[i+1],nums[i])
# 		# print(right)
# 		for i in range(n):
# 			water+=min(left[i],right[i])-nums[i]
# 		print(water)

# if __name__=="__main__":
# 	s=Solution()
# 	s.trapRainWat([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

# class Solution:
# 	def validPar(self,s):
# 		d={")":"(","}":"{","]":"["}
# 		stack=[]
# 		for i in s:
# 			if i in d.values():
# 				stack.append(i)
# 			else:
# 				if not stack or stack[-1]!=d[i]:
# 					print("mismatch")
# 					return
# 		print("match")

# if __name__=="__main__":
# 	s=Solution()
# 	s.validPar("()")
# 	s.validPar("()[]{}")
# 	s.validPar("(])")
# 	s.validPar("[(()]")