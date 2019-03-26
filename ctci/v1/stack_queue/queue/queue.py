from collections import deque


class Queue:
    """implemented for the heck of it"""

    def __init__(self, values=None):
        self.queue = deque()
        if values is not None:
            for i in values:
                self.enqueue(i)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()
