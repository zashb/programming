def main(nums):
    ranges = []
    for i in nums:
        if not ranges or i>ranges[-1][-1]+1:    ranges.append([])
        ranges[-1][1:]=[i]
        # print("ranges:",ranges)
    return ['->'.join(list(map(str, r))) for r in ranges]

if __name__ == '__main__':
    print(main([0,1,2,4,5,7]))
    print(main([0,2,3,4,6,8,9]))