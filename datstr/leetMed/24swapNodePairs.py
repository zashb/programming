class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution:
    def swapNodePairs(self, h):
        if not h or not h.next:
            return h
        n = h.next
        h.next = self.swapNodePairs(h.next.next)
        n.next = h
        return n


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(1)
    print(l1)
    print(s.swapNodePairs(l1))
