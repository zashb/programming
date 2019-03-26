def main(n):
    res = []
    backtrack(res,"",0,0,n)
    return res

def backtrack(res,str,open,close,max):
    if len(str)==max*2: 
        res.append(str)
        return
    if open<max:    backtrack(res,str+"(",open+1,close,max)
    if close<open:  backtrack(res,str+")",open,close+1,max)


if __name__ == '__main__':
    n=3
    print(main(3))