"""
Given a linked list, swap the two nodes present at position `i` and `j`, assuming `0 <= i <= j`.
The positions are based on 0-based indexing.
"""


class Node:
    """LinkedList Node"""

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    if left_index < 0 or right_index <= left_index:
        print("Invalid input for index")

    left_node = None
    left_prev = None
    left_next = None
    right_node = None
    right_prev = None
    right_next = None
    current = head

    for idx in range(left_index):
        if not current:
            print("Invalid input: left_index out of bounds.")

        current = current.next

        if idx == left_index - 2:
            left_prev = current

    left_node = current

    if not current:
        print("Invalid input: right_index out of bounds.")

    left_next = current.next

    for idx in range(right_index - left_index):
        if not current:
            print("Invalid input: right_index out of bounds.")

        right_prev = current
        current = current.next

    right_node = current

    if not right_node:
        print("Invalid input: right_index out of bounds.")

    right_next = right_node.next

    if left_prev:
        left_prev.next = right_node
    else:
        head = right_node

    right_node.next = left_next
    right_prev.next = left_node
    left_node.next = right_next

    return head


def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        print_linked_list(updated_head)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")
        print(e)


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


arr = [9, 2, 3, 4, 5, 6, 7, 8, 1]
head = create_linked_list(arr)
left_index = 0
right_index = 8

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)
