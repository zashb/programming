class Search:
    def sequentialSearch(self, alist, item):
        pos = 0
        # iterate until end of list
        while pos < len(alist):
            # if item != current item, inc pos
            if alist[pos] != item:
                pos += 1
            # if equal, return pos
            else:
                return pos
        return -999

    # if alist is ordered
    def orderedSequentialSearch(self, alist, item):
        pos = 0
        # iterate until EOL
        while pos < len(alist):
            # split inequality into <, >, ==
            # if < ,inc pos
            if alist[pos] < item:
                pos += 1
            else:
                # if >, item not there
                if alist[pos] > item:
                    break
                else:
                    return pos
        return -999

    # if alist is ordered
    def binarySearch(self, alist, item):
        # initialize first and last pointers
        first = 0
        last = len(alist) - 1
        # iterate until EOL
        while first <= last:
            # compute mid
            mid = (first + last) // 2
            # if item < mid elem, last ptr = mid-1
            if item < alist[mid]:
                last = mid - 1
            else:
                # if item > mid elem, first ptr = mid+1
                if item > alist[mid]:
                    first = mid + 1
                else:
                    return mid
        return -999


if __name__ == "__main__":
    # print(Search().sequentialSearch([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3232323223,2,4],4))
    # print(Search().orderedSequentialSearch([0, 1, 2, 8, 13, 17, 19, 32, 42,],13))
    print(Search().binarySearch([0, 1, 2, 8, 13, 17, 19, 32, 42, ], 13))
