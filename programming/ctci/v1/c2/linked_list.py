from random import randint


class LinkedListNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(i) for i in self]
        return " -> ".join(values)

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for i in values:
            self.add(i)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            value = randint(min_value, max_value)
            self.add(value)
        return self


class DoublyLinkedList:
    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value, None, self.tail)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self
