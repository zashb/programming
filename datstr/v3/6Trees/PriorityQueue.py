class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # temp = self.heapList[i//2]
                # self.heapList[i // 2] = self.heapList[i]
                # self.heapList[i] = temp
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def delMin(self):
        # self.heapList[0] == 0 always
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist) // 2
        while (i > 0):
            self.percDown(i)
            i -= 1


if __name__ == "__main__":
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
    print(bh.heapList[1:])
    print(bh.delMin())
    print(bh.heapList[1:])
