# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def __repr__(self):
#         if self:
#             return "{} -> {}".format(self.val, repr(self.next))
#
#
# class Solution:
#     def deleteDups(self, head):
#         if not head:
#             return head
#         if head.next:
#             if head.val != head.next.val:
#                 head.next = self.deleteDups(head.next)
#             else:
#                 head = self.deleteDups(head.next)
#         return head
#
#     def remove_dups_inplace(self, head):
#         curr = head
#         while curr is not None:
#             runner = curr
#             while runner.next is not None:
#                 if runner.next.val != curr.val:
#                     runner = runner.next
#                 else:
#                     # remove if ==
#                     runner.next = runner.next.next
#             curr = curr.next
#         return head
#
#     def remove_nodes_with_dups(self, head):
#         dummy = ListNode(0)
#         previous, current = dummy, head
#         while current:
#             if current.next and current.next.val == current.val:
#                 # assign curr.val to a var and compare all curr.val to val
#                 val = current.val
#                 while current and current.val == val:
#                     current = current.next
#                 previous.next = current
#             else:
#                 previous.next = current
#                 previous = current
#                 current = current.next
#         return dummy.next
#
#
# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(1)
#     head.next.next = ListNode(2)
#     head.next.next.next = ListNode(3)
#     head.next.next.next.next = ListNode(3)
#     # print(Solution().deleteDups(head))
#     # print(Solution().remove_dups_inplace(head))
#     print(Solution().remove_nodes_with_dups(head))

class ListNode:
    def __init__(self, x):
        self.val = x


class Solution:
    def __init__(self):
        self.head = None

    def insertAtHead(self, x):
        newNode = ListNode(x)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def removeDupsFrmSortedList(self):
        if not self.head:
            return
        curr = self.head
        while curr.next:
            if curr.val == curr.next.val:
                # nextNext = curr.next.next
                # curr.next.next = None
                # curr.next = nextNext
                curr.next=curr.next.next
            else:
                curr = curr.next


if __name__ == "__main__":
    l = Solution()
    for i in [20, 13, 13, 11, 11, 11]:
        l.insertAtHead(i)
    print("orig:")
    l.printList()
    l.removeDupsFrmSortedList()
    print("dupsRemoved")
    l.printList()
