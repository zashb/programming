# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def __repr__(self):
#         return "{} -> {}".format(self.val, repr(self.next))
#
#
# class Solution:
#     def revList(self, head):
#         dummy = None
#         while head:
#             curr, head = head, head.next
#             curr.next, dummy = dummy, curr
#         return dummy
#
#
# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     print(Solution().revList(head))

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def revList(self, head):
        # curr, prev = self.head, None
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # self.head = prev

        if head is None:
            return
        self.revList(head.next)
        print(head.val)

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    # s = Solution()
    # for i in [20, 4, 15, 85]:
    #     s.insertAtBeg(i)
    # print("given list:")
    # s.printList()
    # s.revList()
    # print("rev list:")
    # s.printList()

    s = Solution()
    for i in [20, 4, 15, 85]:
        s.insertAtBeg(i)
    print("given list:")
    s.printList()
    print("rev list:")
    s.revList(s.head)


    # TTR:
    # Iterate trough the linked list.
    # In loop, change next to prev, prev to current and current to next
    # recursive:
    # if not head : return
    # recursive step and print in the same order
