# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?



class Solution:
    def candy(self, ratings):
        res = [1] * len(ratings)
        lbase = rbase = 1
        # check if i > i -1
        for i in range(1, len(ratings)):
            lbase = lbase + 1 if ratings[i] > ratings[i - 1] else 1
            res[i] = lbase
        # print(res)
        # check if i > i+1
        for i in range(len(ratings) - 2, -1, -1):
            rbase = rbase + 1 if ratings[i] > ratings[i + 1] else 1
            res[i] = max(rbase, res[i])
        return sum(res)


if __name__ == "__main__":
    print(Solution().candy([1, 2, 3, 2, 3, 5, 2, 5]))

    # TTR:
    # lbase,rbase vars
    # 2 passes 1 for a[i]>a[i-1] , other for a[i]>a[i+1] in the rev
