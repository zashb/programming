class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reorderList(self, head):
        if head == None or head.next == None:
            return head

        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None
        while current != None:
            current.next, prev, current = prev, current, current.next
        dummy = ListNode(0)
        current = dummy

        while head != None and prev != None:
            current.next, current, head = head, head, head.next
            current.next, current, prev = prev, prev, prev.next

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reorderList(head))

    # TTR:
    # fast,slow,curr,prev ptrs
    # update curr,prev.next,prev
    # update curr.next,pre,curr
