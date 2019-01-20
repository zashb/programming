def main(num):
    res,num_abs=0,abs(num)
    while num_abs!=0:
        tail=num_abs%10
        res=tail+res*10
        num_abs//=10
    return res if num>0 else -res

if __name__ == '__main__':
    print(main(123))
    print(main(-123))