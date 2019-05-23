class ArrayQueue:
    # moderate cap for all queues
    DEFAULT_CAPACITY = 10

    # create empty queue
    # _size - curr # elems in queue
    # _front - index of first elem in _data
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    # ret # elems in queue
    def __len__(self):
        return self._size

    # ret if queue is empty
    def is_empty(self):
        return self._size == 0

    # ret first elem
    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self._data[self._front]

    # rem and ret first elem
    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        a = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return a

    # add elem
    def enqueue(self,item):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = item
        self._size += 1

    # resize to new cap
    def resize(self,cap):
        old = self._data
        self._data = [None]*cap
        a = self._front
        for i in range(self._size):
            self._data[i] = old[a]
            a = (a + 1) % len(old)
        self._front = 0


class Empty(Exception):
    pass




if __name__ == "__main__":
    # a = ArrayQueue()
    # for i in range(21,26):
    #     a.enqueue(i)
    # print(a._data)
    from collections import deque
    a = deque()
    for i in range(21,26):
        a.append(i)
    print(a)
    b = a.rotate(1)
    print(b)