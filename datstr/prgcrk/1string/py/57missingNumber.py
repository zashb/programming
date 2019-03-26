def main(nums):
    return set(range(min(nums),max(nums)+1))-set(nums)

if __name__ == '__main__':
    print(main([0,1,3]))
    print(main([10,11,13]))