class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def deleteDuplicates(self, head):
        if not head: return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
        return head

    def printList(self, head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    Solution().printList(head)
    print(Solution().deleteDuplicates(head))

    # TTR:
    # use recursion
#   # if head==head.next then head=recursive(head.next) else head.next=recursive(head.next)