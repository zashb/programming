class LinkedStack:
    class _Node:
        def __init__(self,element,next):
            # ref to elem
            self._element = element
            # ref to next node
            self._next = next

    def __init__(self):
        # ref to head
        self._head = None
        # #stack elems
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self,item):
        # create a new node, add elem to top of stack
        self._head = self._Node(item,self._head)
        # inc size
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty("no elems to pop")
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans




class Empty(Exception):
    pass