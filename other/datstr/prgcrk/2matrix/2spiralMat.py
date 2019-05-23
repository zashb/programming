# get spiral of a given mat
def main(mat):
    return mat and list(mat.pop(0)) + main(list(zip(*mat))[::-1])

if __name__ == '__main__':
    mat = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    print("orig:")
    for i in mat: print(i)
    print("spiral:")
    print(main(mat))