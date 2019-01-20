def main(num):
    res = 0
    while num > 0:
        num //= 5
        res += num
    return res

if __name__ == '__main__':
    for i in [5,100]:   print(main(i))