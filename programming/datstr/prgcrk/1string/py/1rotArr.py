def rotArr(nums, k):
    return nums[k + 1:] + nums[:k + 1]

def revWrds(s):
    s_l = s.split()
    revWrds = " ".join(s_l[::-1])
    return revWrds

if __name__ == '__main__':
    print(rotArr([1, 2, 3, 4, 5, 6, 7], 3))
    print(revWrds("the sky is blue"))