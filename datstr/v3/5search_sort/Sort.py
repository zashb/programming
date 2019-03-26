from collections import deque


class Sort:
    # pushes max elem to right most after each iter
    def bubbleSort(self, alist):
        # swap flag to skip swapless iterations
        swap = True
        passnum = len(alist) - 1
        while passnum > 0 and swap:
            swap = False
            for i in range(passnum):
                if alist[i] > alist[i + 1]:
                    swap = True
                    alist[i + 1], alist[i] = alist[i], alist[i + 1]
            passnum -= 1
        return alist

    # looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location
    def selectionSort(self, alist):
        # outer loop in rev
        for i in range(len(alist) - 1, 0, -1):
            posOfMax = 0
            # inner loop from fwd
            for j in range(1, i + 1):
                if alist[j] > alist[posOfMax]:
                    posOfMax = j
            alist[posOfMax], alist[i] = alist[i], alist[posOfMax]
        return alist

    # It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
    def insertionSort(self, alist):
        for i in range(1, len(alist)):
            currVal = alist[i]
            while i > 0 and alist[i - 1] > currVal:
                alist[i] = alist[i - 1]
                i -= 1
            alist[i] = currVal
        return alist

    # def mergeSort(self, alist):
    #     if len(alist) > 1:
    #         mid = len(alist) // 2
    #         lefthalf = alist[:mid]
    #         righthalf = alist[mid:]
    #         self.mergeSort(lefthalf)
    #         self.mergeSort(righthalf)
    #         i, j, k = 0, 0, 0
    #         while i < len(lefthalf) and j < len(righthalf):
    #             if lefthalf[i] < righthalf[j]:
    #                 alist[k] = lefthalf[i]
    #                 i += 1
    #             else:
    #                 alist[k] = righthalf[j]
    #                 j += 1
    #             k += 1
    #
    #         while i < len(lefthalf):
    #             alist[k] = lefthalf[i]
    #             i += 1
    #             k += 1
    #
    #         while j < len(righthalf):
    #             alist[k] = righthalf[j]
    #             j += 1
    #             k += 1
    #     return alist

    def mergeSort(self, alist):
        if len(alist) == 0 or len(alist) == 1:
            return alist
        else:
            mid = len(alist) // 2
            a = self.mergeSort(alist[:mid])
            b = self.mergeSort(alist[mid:])
            return self.merge(deque(a), deque(b))

    def merge(self, a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a.popleft())
            else:
                c.append(b.popleft())
        if len(a) == 0:
            c += b
        else:
            c += a
        return c


if __name__ == "__main__":
    # print(Sort().bubbleSort([20, 30, 40, 90, 50, 60, 70, 80, 100, 110]))
    # print(Sort().insertionSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
    print(Sort().mergeSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
