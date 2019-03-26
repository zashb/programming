def main(nums):
    first = second = float('inf')
    for i in nums:
        if i<=first:  first=i
        elif i<=second:   second=i
        else:   return True
    return False

if __name__ == '__main__':
    print(main([1, 2, 3, 4, 5]))
    print(main([5, 4, 3, 2, 1]))