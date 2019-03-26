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

    def getCounter(self):
        curr = self.head
        counterDict = {}
        while curr:
            if curr.val not in counterDict:
                counterDict[curr.val] = 1
            else:
                counterDict[curr.val] += 1
            curr = curr.next
        print(counterDict)


if __name__ == "__main__":
    l = Solution()
    for i in [1, 3, 1, 2, 1]:
        l.insertAtHead(i)
    print("list :")
    l.printList()
    print("list counter:")
    l.getCounter()
