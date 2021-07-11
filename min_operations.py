"""
Using only multiplication by 2 and addition by 1, find the minimum number 
of steps required to reach a number.
"""

def min_operations(target):
    steps = 0
    
    # starting backwards from the target
    # if target is odd, subtract 1
    # if target is even, divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        steps += 1
    return steps

# Test Cases
def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)

target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)
