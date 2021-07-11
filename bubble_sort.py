def bubble_sort_1(l):
    l_copy = list.copy(l)

    while True:
        is_sorted = True

        for i in range(len(l_copy) - 1):
            if l_copy[i] > l_copy[i + 1]:
                l_copy[i], l_copy[i + 1] = l_copy[i + 1], l_copy[i]
                is_sorted = False
                
        if is_sorted:
            return l_copy


def bubble_sort_2(l):
    l_copy = list.copy(l)

    for _ in range(len(l_copy)):
        for index in range(1, len(l_copy)):
            this = l_copy[index]
            prev = l_copy[index - 1]

            if prev <= this:
                continue

            l_copy[index] = prev
            l_copy[index - 1] = this

    return l_copy



def test_helper(func):
    unsorted_list = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
    sorted_list = func(unsorted_list)
    print ("Pass" if (sorted_list[0] == 3) else "Fail")

test_helper(bubble_sort_1)
test_helper(bubble_sort_2)
