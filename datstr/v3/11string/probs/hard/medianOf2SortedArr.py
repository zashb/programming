class Solution:
    def findMedianSortedArrays(self, A, B):
        totLen = len(A) + len(B)
        if totLen % 2 == 1:
            return self._kth(A, B, totLen // 2)
        else:
            return (self._kth(A, B, totLen // 2) + self._kth(A, B, totLen // 2 - 1)) / 2.

    def _kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        medianIndexA, medianIndexB = len(a) // 2, len(b) // 2
        medianA, medianB = a[medianIndexA], b[medianIndexB]

        if k > medianIndexA + medianIndexB:
            # if a's median is bigger than b's, b's first half doesn't include k
            if medianA > medianB:
                return self._kth(a, b[medianIndexB + 1:], k - medianIndexB - 1)
            else:
                return self._kth(a[medianIndexA + 1:], b, k - medianIndexA - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if medianA > medianB:
                return self._kth(a[:medianIndexA], b, k)
            else:
                return self._kth(a, b[:medianIndexB], k)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

    # TTR:
    # helper method _kth to which A,B,mid are passed when even or odd lengths of input
    # if median idx > median idx of a + idx of b
