class Node:
    # data,next,getters,setters
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class LinkedList:
    # linkedlist identified by head
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    # making the linked list iterable
    def __iter__(self):
        node = a.head
        while node:
            yield node
            node = node.next

    def insertAtBeg(self, data):
        # instantiate new node
        newNode = Node()
        # set data
        newNode.setData(data)
        # if linked list is empty, head = newNode
        if self.len == 0:
            self.head = newNode
        else:
            # update newnode's next, update head
            newNode.setNext(self.head)
            self.head = newNode
        # inc len anyways
        self.len += 1

    def revLinkedList(self):
        last = None
        current = self.head
        while current is not None:
            nextNode = current.getNext()
            current.setNext(last)
            last = current
            current = nextNode
        self.head = last


class Solution:
    def nthnodefromend(self, head, n):
        # dict to get posn : val
        d = {}
        current = head
        position = 0
        while current is not None:
            d[position] = current.getData()
            position += 1
            current = current.getNext()
        result = []
        result.append(d)
        result.append(d[len(d) - n])
        return result


if __name__ == "__main__":
    a = LinkedList()
    for i in range(11, 16):
        a.insertAtBeg(i)
    print("head of linked list :{}".format(a.head.getData()))
    print("len of linked list : {}".format(a.len))
    print("linked list : {}".format([i.getData() for i in a]))
    print("linked list with positions :{0},  nth node from end :{1}".format(Solution().nthnodefromend(a.head, 1)[0],
                                                                            Solution().nthnodefromend(a.head, 1)[1]))
    a.revLinkedList()
    print("reversed linked list :{}".format([i.getData() for i in a]))
    a.revLinkedList()
    print("re-reversing linked list :{}".format([i.getData() for i in a]))
