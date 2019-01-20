class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    # def insertAtHead(self, x):
    #     newNode = ListNode(x)
    #     newNode.next = self.head
    #     self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def sortedInsert(self, newNode):
        # if no elem, make it head
        if self.head is None:
            newNode.next = self.head
            self.head = newNode
        # if new elem <= head, make it head
        elif self.head.val >= newNode.val:
            newNode.next = self.head
            self.head = newNode
        # if new elem > head, traverse until next < new elem
        else:
            curr = self.head
            while curr.next and curr.next.val < newNode.val:
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode


if __name__ == "__main__":
    l = Solution()
    for i in [5, 10, 7, 3, 1, 9]:
        # l.insertAtHead(i)
        l.sortedInsert(ListNode(i))
    print("sorted list :")
    l.printList()
