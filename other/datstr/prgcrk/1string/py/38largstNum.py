import itertools

def main(nums):
    nums_s = [str(i) for i in nums]
    nums_s_perm = list(itertools.permutations(nums_s))
    nums_s_perm_joind = ["".join(i) for i in nums_s_perm ]
    # return max(list(map(lambda x:int(x),nums_s_perm_joind)))
    return max(nums_s_perm_joind)

if __name__ == '__main__':
    print(main([3, 30, 34, 5, 9]))