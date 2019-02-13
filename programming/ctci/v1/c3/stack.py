import unittest

from programming.ctci.v1.c2.linked_list import LinkedList


class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if self.stack is not None:
            self.stack.append(item)

    def pop(self):
        if self.is_empty(self.stack):
            return None
        return self.stack.pop()

    def is_empty(self, stack):
        return len(stack) == 0


class StackLL:
    def __init__(self):
        self.ll = LinkedList()

    def is_empty(self, ll):
        if ll.head is None:
            return True
        else:
            return False

    def push(self, item):
        self.ll.add(item)

    def pop(self):
        if not self.is_empty(self.ll):
            temp = self.ll.head
            self.ll.head = self.ll.head.next
            return temp.value
        else:
            return None


class Test(unittest.TestCase):
    def test_stacklist(self):
        sl = StackList()
        self.assertTrue(sl.is_empty(sl.stack))
        for i in range(3):
            sl.push(i)
        self.assertFalse(sl.is_empty(sl.stack))
        self.assertEqual(sl.pop(), 2)

    def test_stackLL(self):
        sll = StackLL()
        self.assertTrue(sll.is_empty(sll.ll))
        for i in range(3):
            sll.push(i)
        self.assertFalse(sll.is_empty(sll.ll))
        self.assertEqual(sll.pop(), 0)
