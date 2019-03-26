def main(n):
    res = []
    for i in range(n):
        res.append([1]*(i+1))
        if i>1 :    
            for j in range(1,i):    res[i][j]=res[i-1][j-1]+res[i-1][j]
    return res

if __name__ == '__main__':
    n = 5
    print(main(n))