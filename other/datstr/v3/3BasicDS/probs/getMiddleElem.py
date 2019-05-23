class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def getMiddleElem(self):
        slowP, fastP = self.head, self.head
        while fastP and fastP.next:
            fastP = fastP.next.next
            slowP = slowP.next
        print(slowP.val)


if __name__ == "__main__":
    l = Solution()
    for i in [10, 30, 11, 21, 14]:
    # for i in [10, 30, 11, 21, 14, 16]:
        l.insertAtHead(i)
    print("list :")
    l.printList()
    print("middle elem:")
    l.getMiddleElem()
