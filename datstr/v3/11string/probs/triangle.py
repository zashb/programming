class Solution:
    def minTotal(self,triangle):
        minList = [min(i) for i in triangle]
        return sum(minList)


if __name__=="__main__":
    print(Solution().minTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))