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

    def getElem(self, x):
        curr = self.head
        while curr:
            if curr.val == x:
                print(curr.val)
                return
            else:
                curr = curr.next
        print("elem not found")


if __name__ == "__main__":
    l = Solution()
    for i in [10, 30, 11, 21, 14]:
        l.insertAtHead(i)
    print("list :")
    l.printList()
    print("found elem:")
    l.getElem(21)
