# Given a m * n matrix, if an element is 0, set its entire row and column to 0.

def main(mat):
    rows,cols,col0 = len(mat),len(mat[0]),1
    for i in range(rows):
        if mat[i][0] == 0: col0 = 0
        for j in range(1,cols):
            if mat[i][j] == 0:
                mat[i][0] = mat[0][j] = 0
    for i in range(rows-1,-1,-1):
        for j in range(cols-1,0,-1):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
        if col0 == 0: mat[i][0] = 0
    return(mat)

if __name__ == '__main__':
    mat = [[1,1,1,0],[1,1,1,0],[1,1,0,0],[1,0,0,0]]
    print(main(mat))