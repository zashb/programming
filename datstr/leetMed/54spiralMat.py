def spiralMat(A):
    res = []
    if len(A) == 0:
        return res
    rowBeg, rowEnd, colBeg, colEnd = 0, len(A) - 1, 0, len(A[0]) - 1
    while rowBeg <= rowEnd and colBeg <= colEnd:
        for i in range(colBeg, colEnd + 1):
            res.append(A[rowBeg][i])
        rowBeg += 1
        for i in range(rowBeg, rowEnd + 1):
            res.append(A[i][colEnd])
        colEnd -= 1
        if rowBeg <= rowEnd:
            for i in range(colEnd, colBeg - 1, -1):
                res.append(A[rowEnd][i])
        rowEnd -= 1
        if colBeg <= colEnd:
            for i in range(rowEnd, rowBeg - 1, -1):
                res.append(A[i][colBeg])
        colBeg += 1
    return res


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(spiralMat(A))

# simple straight forward ans
