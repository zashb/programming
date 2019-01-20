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
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         # crazy step - ref for 0
#         curr = dummy = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         curr.next = l1 or l2
#         return dummy.next
#
#
# if __name__ == "__main__":
#     l1 = ListNode(0)
#     l1.next = ListNode(2)
#     l2 = ListNode(1)
#     l2.next = ListNode(3)
#     print(Solution().mergeTwoLists(l1, l2))


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


class Solution:
    def mergeLists(self, l1, l2):
        curr = None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            curr = l1
            curr.next = self.mergeLists(l1.next, l2)
        else:
            curr = l2
            curr.next = self.mergeLists(l1, l2.next)
        return curr

    def printList(self, temp1):
        self.temp2 = temp1
        while self.temp2 != None:
            print(self.temp2.val)
            self.temp2 = self.temp2.next


if __name__ == "__main__":
    print('first list is: ')
    llist1 = List()
    llist1.insertAtBeg(301)
    llist1.insertAtBeg(99)
    llist1.insertAtBeg(75)
    llist1.insertAtBeg(55)
    llist1.insertAtBeg(16)
    llist1.insertAtBeg(2)
    llist1.printList()
    print('second list is: ')
    llist2 = List()
    llist2.insertAtBeg(299)
    llist2.insertAtBeg(103)
    llist2.insertAtBeg(89)
    llist2.insertAtBeg(57)
    llist2.insertAtBeg(19)
    llist2.insertAtBeg(10)
    llist2.printList()

    print('sorted list is: ')
    llist3 = List()
    s = Solution()
    llist3.head = s.mergeLists(llist1.head, llist2.head)
    s.printList(llist3.head)

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def __init__(self):
#         self.head = None
#
#     def insertAtBeg(self, x):
#         newNode = ListNode(x)
#         newNode.next = self.head
#         self.head = newNode
#
#     def printList(self):
#         curr = self.head
#         while curr:
#             print(curr.val)
#             curr = curr.next
#
#
#
# if __name__ == "__main__":
#     l1, l2 = Solution(), Solution()
#     for i in [5, 10, 15]:
#         l1.insertAtBeg(i)
#     print("l1:")
#     l1.printList()
#     for i in [2, 10, 20]:
#         l2.insertAtBeg(i)
#     print("l2:")
#     l2.printList()
#
