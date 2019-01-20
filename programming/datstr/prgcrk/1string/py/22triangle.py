def triangle(n):
	row_min=[min(i) for i in n]
	return sum(row_min)

if __name__=="__main__":
	print(triangle([[2],[3,4],[6,5,7],[4,1,8,3]]))