class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head

        while node.next is not None:
            node = node.next

        node.next = Node(value)

    def to_list(self):
        out = []
        node = self.head

        while node:
            out.append(int(str(node.value)))
            node = node.next
        return out


def merge(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    node1 = list1.head
    node2 = list2.head
    merged_list = LinkedList(None)

    while node1 or node2:
        if node1 is None:
            merged_list.append(node2.value)
            node2 = node2.next
        elif node2 is None:
            merged_list.append(node1.value)
            node1 = node1.next
        elif node1.value <= node2.value:
            merged_list.append(node1.value)
            node1 = node1.next
        elif node1.value > node2.value:
            merged_list.append(node2.value)
            node2 = node2.next

    return merged_list


class NestedLinkedList(LinkedList):
    """
    In a NESTED LinkedList object, each node will be a simple LinkedList in itself
    """

    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next:
            return merge(node.value, self._flatten(node.next))

        return merge(node.value, None)

# tests
list1 = LinkedList(Node(1))
list1.append(3)
list1.append(4)

list2 = LinkedList(Node(2))
list2.append(5)

expected_merge = LinkedList(Node(1))
expected_merge.append(2)
expected_merge.append(3)
expected_merge.append(4)
expected_merge.append(5)

performed_merge = merge(list1, list2)

print(expected_merge.to_list())
print(performed_merge.to_list())

assert performed_merge.to_list() == expected_merge.to_list(), "merge failed"

nested = NestedLinkedList(Node(list1))
nested.append(list2)

print(nested.flatten().to_list())

assert nested.flatten().to_list() == expected_merge.to_list(), "flatten failed"
