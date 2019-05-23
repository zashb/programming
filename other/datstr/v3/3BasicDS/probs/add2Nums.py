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

    def addTwoLists(self, l1, l2):
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while l1 is not None or l2 is not None:
            l1Val = 0 if l1 is None else l1.val
            l2Val = 0 if l2 is None else l2.val
            _sum = carry + l1Val + l2Val
            # update carry for next calculation
            carry = 1 if _sum >= 10 else 0
            # update sum if it is greater than 10
            _sum = _sum if _sum < 10 else _sum % 10
            # Create a new node with sum as data
            temp = ListNode(_sum)
            # if this is the first node then set it as head of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
                # Set prev for next insertion
            prev = temp
            # Move l1 and l2 pointers to next nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            temp.next = ListNode(carry)

    # Utility function to print the linked LinkedList
    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    l1, l2 = Solution(), Solution()
    for i in [6, 4, 9, 5, 7]:
        l1.insertAtBeg(i)
    print("l1:")
    l1.printList()
    for i in [4, 8]:
        l2.insertAtBeg(i)
    print("l2:")
    l2.printList()
    res = Solution()
    res.addTwoLists(l1.head, l2.head)
    print("res:")
    res.printList()

    # TTR:
    # pass l1.head and l2.head to addTwoLists
    # init prev,temp,carry
    # l1Val = 0 if not l1 else l1.val
    # temp = ListNode(_sum)
    # prev = temp
