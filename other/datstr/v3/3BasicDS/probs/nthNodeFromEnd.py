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

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def nthFromEnd(self, n):
        mainPtr, refPtr, count = self.head, self.head, 0
        if self.head is not None:
            while count < n:
                if refPtr is None:
                    print("{} is greater than #nodes in the list".format(n))
                    return
                refPtr = refPtr.next
                count += 1
        while refPtr is not None:
            mainPtr = mainPtr.next
            refPtr = refPtr.next
        # print("node {} from end is {}".format(n, mainPtr.val))
        return mainPtr.val

if __name__ == "__main__":
    s = Solution()
    s.insertAtBeg(20)
    s.insertAtBeg(4)
    s.insertAtBeg(15)
    s.insertAtBeg(35)
    print("list:")
    s.printList()
    n = 3
    print("{} node from end".format(n))
    print(s.nthFromEnd(n - 1))

    # TTR:
    # Initialize both reference and main pointers to head.
    # First move reference pointer to n nodes from head.
    # Now move both pointers one by one until reference pointer reaches end.
    # Now main pointer will point to nth node from the end. Return main pointer.
