class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.current_size = 0
        self.head = None

    def push(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.current_size += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.current_size -= 1

        return value

    def size(self):
        return self.current_size

    def top(self):
        if self.is_empty():
            return None

        return self.head.value

    def is_empty(self):
        return self.size() == 0


class ArrayStack:
    """
    Note that this implements the stack with an Array as strictly defined:
    an ordered, indexed collection of known length
    """

    def __init__(self, initial_size=10):
        self.arr = [0 for values in range(0, initial_size)]
        self.next_index = 0
        self.max_size = initial_size

    def _handle_stack_overflow(self):
        print('Out of space! Increasing stack capacity...')
        self.max_size += 10
        self.arr.extend([0 for values in range(0, 10)])

    def push(self, elem):
        if self.next_index >= self.max_size:
            self._handle_stack_overflow()

        self.arr[self.next_index] = elem
        self.next_index += 1

    def pop(self):
        if self.next_index > 0:
            elem = self.arr[self.next_index - 1]
            self.arr[self.next_index - 1] = 0
            self.next_index -= 1

            return elem
        else:
            return None

    def size(self):
        return self.next_index

    def top(self):
        return self.arr[self.next_index - 1]

    def is_empty(self):
        return self.next_index == 0
