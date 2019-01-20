# heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,
# smallest element is always the root, heap[0].

import heapq


class Solution:
    def kthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]

        # doubtful about the output
        # heap = []
        # for i in nums:
        #     heapq.heappush(heap, i)
        # print(heap)
        # for _ in range(len(nums) - k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)


if __name__ == "__main__":
    print(Solution().kthLargest([3, 1, 2, 5, 6, 4], 2))

    # TTR:
    # pop loop until len(nums)-k
