class Solution:
    def largestRectArea(self, heightList):
        heightList.append(0)
        idxStack = [-1]
        res = 0
        for idx, height in enumerate(heightList):
            while height < heightList[idxStack[-1]]:
                h = heightList[idxStack.pop()]
                w = idx - idxStack[-1] - 1
                res = max(res, h * w)
            idxStack.append(idx)
        heightList.pop()  # better practice
        return res


if __name__ == "__main__":
    print(Solution().largestRectArea([2, 1, 5, 6, 3, 2]))

    # The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building which are taller than the new one. The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings

    # TTR:
    # heightList.append(0)
    # idxStack=[-1]
    # pop for height
    # h=heightList[idxStack.pop()]; w=idx-idxStack[-1]-1; res=max(res,h*w)
