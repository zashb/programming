class Solution:
    def minSizeSubarrSum(self, nums, s):
        if s in nums:
            return 1
        else:
            for i, j in enumerate(nums):
                if i < len(nums) - 1:
                    combs = self.combinations(nums, i)
                    # print(i, "\n", list(combs))
                    combsSum = [sum(k) for k in combs]
                    # print(combsSum)
                    if s in combsSum:
                        return i

    # combinations implementation
    def combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    print(Solution().minSizeSubarrSum([2, 3, 1, 2, 4, 3], 7))

