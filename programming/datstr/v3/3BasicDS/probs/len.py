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

    def getLength(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        print(count)


if __name__ == "__main__":
    l = Solution()
    for i in [1, 3, 1, 2, 1]:
        l.insertAtHead(i)
    print("list :")
    l.printList()
    print("length:")
    l.getLength()
