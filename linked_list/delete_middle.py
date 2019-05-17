import unittest

from ctci.v1.linked_list.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_delete_middle(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 3, 4])
        middle_node = ll.add(5)
        ll.add_multiple([7, 8, 9])
        print("before deletion ll : {}".format(ll))
        print("length before deletion ll : {}".format(len(ll)))
        delete_middle_node(middle_node)
        print("after deletion ll : {}".format(ll))
        print("length after deletion ll : {}".format(len(ll)))

    def test_delete_middle_2(self):
        ll = LinkedList()
        ll.add_multiple([1, 2, 3, 4])
        middle_node = ll.add(5)
        ll.add_multiple([7, 8, 9])
        print("before deletion ll : {}".format(ll))
        print("length before deletion ll : {}".format(len(ll)))
        delete_middle_node_2(middle_node)
        print("after deletion ll : {}".format(ll))
        print("length after deletion ll : {}".format(len(ll)))


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


def delete_middle_node_2(node):
    if not node or not node.next:
        return False
    next = node.next
    node.data = next.value
    node.next = next.next
    return True


if __name__ == "__main__":
    unittest.main()
