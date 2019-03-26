# def main(num):
#     return num==revInt(num)

# def revInt(num):
#     res,num_abs=0,abs(num)
#     while num_abs!=0:
#         tail=num_abs%10
#         res=res*10+tail
#         num_abs//=10
#     return res if num>0 else -res

def main(num):
    if num < 0 or (num!=0 and num%10 == 0): return False
    rev = 0
    while num > rev:
        rev = rev*10 + num%10
        num//=10
    return num == rev or num == rev//10

if __name__ == '__main__':
    print(main(121))
    print(main(123))