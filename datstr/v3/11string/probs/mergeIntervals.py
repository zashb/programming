class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution:
    def mergeIntervals(self, intervals):
        if not intervals:
            return intervals
        # sort list on start
        intervals = sorted(intervals, key=lambda x: x.start)
        # init result with first interval
        result = [intervals[0]]
        for idx, currInterval in enumerate(intervals):
            # if idx > 0:
                prev = result[-1]
                if currInterval.start <= prev.end:
                    prev.end = max(prev.end, currInterval.end)
                else:
                    result.append(currInterval)
        return result


if __name__ == "__main__":
    print(Solution().mergeIntervals([Interval(1, 3), Interval(2, 6), Interval(15, 18), Interval(8, 10)]))

    # TTR:
    # init res with intervals[0]
    # init prev with res[-1]
    # curr.start<=prev.end
