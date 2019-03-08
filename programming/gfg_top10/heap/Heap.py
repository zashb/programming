import heapq
import unittest


class Heap:
    def __init__(self):
        self.heap = []

    def insert_key(self, key):
        heapq.heappush(self.heap, key)

    def get_min(self):
        # by default heapq is min heap
        return heapq.heappop(self.heap)

    def peek_min(self):
        return self.heap[0]

    def get_k_min(self, k):
        return heapq.nsmallest(k, self.heap)

    def get_k_max(self, k):
        return heapq.nlargest(k, self.heap)


class Test(unittest.TestCase):
    def test(self):
        heapobj = Heap()
        for i in [3, 2, 15, 4, 45, 5]:
            heapobj.insert_key(i)
        print("heap : {}".format(heapobj.heap))
        print("min : {}".format(heapobj.peek_min()))
        k = 3
        print("{} min elems : {}".format(k, heapobj.get_k_min(k)))
        print("{} max elems : {}".format(k, heapobj.get_k_max(k)))
