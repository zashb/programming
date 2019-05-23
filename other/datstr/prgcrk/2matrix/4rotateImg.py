# clockwise rotate
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3

def main(mat):
    mat_rev = mat[::-1]
    # for i in range(len(mat)):
    #     for j in range(i + 1, len(mat[i])):
    #         mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    mat_t = list(zip(*mat_rev))
    return mat_t

if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(main(mat))