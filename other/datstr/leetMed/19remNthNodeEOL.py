class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution:
    def remNthNodeEOL(self, h, n):
        # f = s = h
        # for _ in range(n):
        #     f = f.next
        # if not f:
        #     return h.next
        # while f.next:
        #     f = f.next
        #     s = s.next
        # s.next = s.next.next
        # return h

        s = f = h
        for i in range(n + 1):
            f = f.next
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return h


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(1)
    print(l1)
    print(s.remNthNodeEOL(l1, 2))

    # note
    # Move one pointer fast --> n+1 places forward, to maintain a gap of n between the two pointers and then move both at the same speed. Finally, when the fast pointer reaches the end, the slow pointer will be n+1 places behind - just the right spot for it to be able to skip the next node.
    # Since the question gives that n is valid, not too many checks have to be put in place. Otherwise, this would be necessary.
