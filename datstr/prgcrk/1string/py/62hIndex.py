def main(citations):
    if len(citations)==0:   return 0
    a=[0]*(len(citations)+1)
    for i in range(len(citations)):
        if citations[i]>len(citations): a[len(citations)]+=1
        else:   a[citations[i]]+=1
    t,res=0,0
    for i in range(len(citations),0,-1):
        t+=a[i]
        if t>=i:    return i
    return 0

if __name__ == '__main__':
    print(main([3, 0, 6, 1, 5]))