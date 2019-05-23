class Solution:
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        pos, bal = 0, 0
        for i, j in enumerate(gas):
            bal += j - cost[i]
            if bal < 0:
                pos, bal = i + 1, 0
        return pos


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1, 2, 3], [3, 2, 1]))
    print(Solution().canCompleteCircuit([1, 2, 3], [2, 2, 2]))
    print(Solution().canCompleteCircuit([1, 2, 3], [1, 2, 3]))
    print(Solution().canCompleteCircuit([1, 2, 3], [1, 2, 4]))
