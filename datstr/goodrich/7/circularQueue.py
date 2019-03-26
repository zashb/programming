class CircularQueue:
    class _Node:
        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        head =  self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            # bypass oldhead
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self,element):
        newest = self._Node(element,None)
        if self.is_empty():
            newest._next = newest
        else:
            # new node points to head
            newest._next = self._tail._next
            # old tail points to new node
            self._tail._next = newest
        # new node becomes the tail
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


class Empty(Exception):
    pass