def zigzag(s,nrows):
	rows,rows_idx,step = [""]*nrows,0,-1
	for i in s:
		rows[rows_idx] += i
		if rows_idx in [0,nrows-1]:	step = -step
		rows_idx+=step
	return "".join(rows)

if __name__ == "__main__":
	print(zigzag("PAYPALISHIRING", 3))

# algo
# rows,row_idx,idx