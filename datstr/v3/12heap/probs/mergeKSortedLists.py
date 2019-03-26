import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def mergeKSortedLists(self, lists):
        heap = []
        dummy = ListNode(0)
        curr = dummy
        for i in lists:
            if i:
                heapq.heappush(heap, (i.val, i))
        while heap:
            smallest = heapq.heappop(heap)[1]
            curr.next = smallest
            curr = curr.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(13)
    print(l1)
    l2 = ListNode(2)
    l2.next = ListNode(14)
    print(l2)
    l3 = ListNode(5)
    l3.next = ListNode(25)
    l3.next.next = ListNode(35)
    print(l3)
    print(Solution().mergeKSortedLists([l1, l2, l3]))
