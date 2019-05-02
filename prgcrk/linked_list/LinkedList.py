class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def __str__(self):
        values = [str(i) for i in self]
        return " -> ".join(values)

    def add(self, val):
        node = LinkedListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self.tail

    def add_to_beg(self, val):
        node = LinkedListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        return self.head
