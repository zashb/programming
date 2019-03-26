# def jumpGame(nums):
#     p = 0
#     while p < len(nums):
#         if nums[p]:
#             if p + nums[p] < len(nums) - 1:
#                 p += nums[p]
#             elif p + nums[p] == len(nums) - 1:
#                 return True
#         else:
#             break
#     return False

def jumpGame(nums):
    m = 0
    for i, j in enumerate(nums):
        if i > m:
            return False
        m = max(m, i + j)
    return True


if __name__ == '__main__':
    print(jumpGame([2, 3, 1, 1, 4]))
    print(jumpGame([3, 2, 1, 0, 4]))
