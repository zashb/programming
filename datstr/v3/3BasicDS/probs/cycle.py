# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class Solution:
#     def hasCycle(self, head):
#         # 2pts fast and slow
#         slow, fast = head, head
#         while fast and fast.next:
#             fast, slow = fast.next.next, slow.next
#             # if fast and slow point to same obj
#             if fast is slow:
#                 return True
#         return False
#
#
# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = head.next
#     print(Solution().hasCycle(head))


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insertAtHead(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def hasCycle(self):
        slowP, fastP = self.head, self.head
        while slowP and fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if slowP == fastP:
                return True
        return False

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    s = Solution()
    for i in [20, 4, 15, 10]:
        s.insertAtHead(i)
    print("given list:")
    s.printList()

    print(s.hasCycle())

    s.head.next.next = s.head.next
    print(s.hasCycle())


    # TTR:
    # 2 ptrs fast,slow
    # if fast is slow
    # inserting cycle by l1.head.next = l1.head.next.next
