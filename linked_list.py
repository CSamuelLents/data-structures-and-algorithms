class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        node = self.head

        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    def to_list(self):
        return self.__repr__()

    def incrementSize(self):
        self.size += 1

    def decrementSize(self):
        self.size -= 1

    def reverse(self):
        node = self.head
        previous = None

        while node:
            current, node = node, node.next
            current.next, previous = previous, current

        self.head, self.tail = self.tail, self.head

    def append(self, value):
        node = value if type(value) is Node else Node(value)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.incrementSize()

    def prepend(self, value):
        node = value if type(value) is Node else Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.incrementSize()

    def insertAtIndex(self, value, pos):
        current_node = self.head
        previous_node = None
        index = 0

        while current_node and index < pos:
            if index > 0:
                previous_node = current_node

            current_node = current_node.next
            index += 1

        node = Node(value)
        node.next = current_node

        if previous_node:
            previous_node.next = node

        self.incrementSize()

    def insert(self, value, pos):
        if pos < 0:
            return print(f'Cannot insert at negative index {pos}')

        if pos >= self.size or pos == self.size - 1:
            self.append(value)
        else:
            self.insertAtIndex(value, pos)

    def remove(self, value):
        previous_node, found_node = self.searchWithPrevious(value)

        if not found_node:
            print(f'No node found with value {value}')
            return

        if previous_node:
            previous_node.next = found_node.next
        else:
            self.head = found_node.next
        self.decrementSize()

    def pop(self):
        if not self.head:
            print(f'No node found at head. Calling pop on empty list!')
            return

        popped = self.head
        self.head = self.head.next
        self.decrementSize()
        return popped

    def traverse(self, func):
        node = self.head

        while node:
            if func:
                func(node)
            node = node.next

    def searchWithPrevious(self, value):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.value == value:
                return previous_node, current_node

            previous_node = current_node
            current_node = current_node.next

        return None, None

    def search(self, value):
        _match_prev, match = self.searchWithPrevious(value)

        return match
