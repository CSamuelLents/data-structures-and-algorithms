"""
# Knapsack Problem
Use dynamic programming to implement the function `knapsack_max_value()` to **return the maximum total value**  of items that can be accommodated into the given knapsack.
"""

import collections

Item = collections.namedtuple('Item', ['weight', 'value'])

"""

### The Naive Approach - Based on Recursion:
The idea is, for each given item, if the item-weight is less than the remaining capacity (kg) of the knapsack, then calculate the value ($\$$) of the knapsack if we:
1. **Do not put the item in the knapsack** - Value ($\$$) of the knapsack will be the output of the `knapsack_recursive()` function, with the same remaining capacity, and check for the next item down the list.  
1. **Put the item in the knapsack** - Value ($\$$) of the knapsack will be the **sum** of the current value of the item and output of the `knapsack_recursive()` function,  with **updated** remaining capacity, and check for the next item down the list.  

Return the **maximum of either of the above two values**. In `knapsack_recursive()` function, begin with developing the solution for the base case i.e., smallest subproblem. 

**Note** - Below is the implementation of this naive approach with recursion, that has an exponential time complexity as $O(2^n)$, where $n$ is the number of given items, because we are evaluating both the two options (put/not put) for each given item.
"""

# Naive Approach based on Recursion
def knapsack_max_value(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)


def knapsack_recursive(capacity, items, lastIndex):
    # Base case
    if (capacity <= 0) or (lastIndex<0):
        return 0
    
    # Put the item in the knapsack
    valueA = 0
    if (items[lastIndex].weight <= capacity):
        valueA = items[lastIndex].value + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    
    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)
    
    # Pick the maximum of the two results
    result = max(valueA, valueB)
    
    return result

"""
### Dynamic Programming Approach
Memoize the intermediate results in a lookup table. Start with initializing a lookup
 table (a list), where the index represents the remaining capacity (kg) of the knapsack, 
 and the element represents the maximum value ($\$$) that it can hold. 

**Note** - This approach with dynamic programming will have a time complexity as 
$O(2nC) \equiv O(nC)$, where $n$ is the number of given items and $C$ is the max capacity (kg) of the knapsack. 
"""

# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value(knapsack_max_weight, items):
    # Initialize a lookup table to store the maximum value ($) 
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:
        # The "capacity" represents amount of remaining capacity (kg) of knapsack at a given moment. 
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]

tests = [
    {
        'correct_output': 14,
        'input': {
            'knapsack_max_weight': 15,
            'items': [Item(10, 7), Item(9, 8), Item(5, 6)],
        },
    },
    {
        'correct_output': 13,
        'input': {
            'knapsack_max_weight': 25,
            'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)],
        },
    }
]

for test in tests:
    print("Pass" if test['correct_output'] == knapsack_max_value(**test['input']) else "Fail")

