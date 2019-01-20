import collections
# find the minimum window in s which will contain all the characters in t

def minWinSubstr(s,subStr):
	need, missing = collections.Counter(subStr), len(subStr)
	i = I = J = 0
	for j in range(len(s)):
		missing-=need[s[j]]>0
		need[s[j]]-=1
		if not missing:
			while i<j and need[s[i]]<0:
				need[s[i]]+=1
				i+=1
			if not J or j-i<=J-I:	I,J=i,j
	return s[I:J+1]

if __name__ == "__main__":
	print(minWinSubstr("ADOBECODEBANC","ABC"))

n,m=collections.Counter(subStr),len(subStr)
i=I=J=0
