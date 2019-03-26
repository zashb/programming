def main(n):
    slow,fast = n,n
    # do while loop
    while True:
        slow,fast = digSqSum(slow),digSqSum(fast)
        fast =  digSqSum(fast)
        if slow == fast: break
    return bool(slow == 1)
    # return True if slow == 1 else False

def digSqSum(n):
    sum = 0
    while n:
        dig = n%10
        sum += dig*dig
        n //= 10
    return sum

if __name__ == '__main__':
    print(main(19))
    print(main(29))