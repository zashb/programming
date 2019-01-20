import collections


class Solution:
    def rotateArray(self, nums, k):
        # return nums[k + 1:] + nums[:k + 1]

        deque = collections.deque(nums)
        # for _ in range(k):
        #     deque.appendleft(deque.pop())
        # return list(deque)

        for _ in range(k + 1):
            deque.append(deque.popleft())
        return list(deque)


if __name__ == "__main__":
    print(Solution().rotateArray([1, 2, 3, 4, 5, 6, 7], 3))
