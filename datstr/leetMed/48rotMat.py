# def rotMat(A):
#     print(A)
#     A[:] = zip(*A[::-1])
#     return A

def rotMat(A):
    A = A[::-1]
    for i in range(len(A)):
        for j in range(i + 1, len(A[i])):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotMat(A))

# clockwise rotate
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3
