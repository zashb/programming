import unittest

from programming.ctci.v1.c2.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_partition(self):
        ll = LinkedList()
        ll.generate(10, 0, 99)
        print("before : {}".format(ll))
        partition_key = ll.head.value
        partition(ll, partition_key)
        print("with partition key : {}, after : {}".format(partition_key, ll))


def partition(ll, x):
    current = ll.tail = ll.head
    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            # current.next = ll.head
            # ll.head = current
            ll.add_to_beginning(current.value)
        else:
            # ll.tail.next = current
            # ll.tail = current
            ll.add(current.value)
        current = nextNode
    # Error check in case all nodes are less than x
    # if ll.tail.next is not None:
    #     ll.tail.next = None


if __name__ == "__main__":
    unittest.main()
