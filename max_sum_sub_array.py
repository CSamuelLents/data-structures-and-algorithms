"""
Helper - Find the max crossing sum w.r.t. middle index
"""
def maxCrossingSum(arr, start, mid,  stop):
    """
    LEFT PHASE - Traverse the Left part starting from mid element
    """
    leftSum = arr[mid]
    leftMaxSum = arr[mid]
    
    # Traverse in reverse direction from (mid-1) to start 
    for i in range(mid-1, start-1, -1): 
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum): 
            leftMaxSum = leftSum
    
    """
    RIGHT PHASE - Traverse the Right part, starting from (mid+1)
    """
    rightSum = arr[mid+1]
    rightMaxSum = arr[mid+1]
    
    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid+2, stop+1): 
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum): 
            rightMaxSum = rightSum

    """
    Both rightMaxSum and lefttMaxSum each would contain value of at least one element from the arr
    """
    return (rightMaxSum + leftMaxSum)

"""
Recursive version
"""
def maxSubArrayRecursive(arr, start, stop): 
    # Base case
    if (start==stop):
        return arr[start]

    if(start < stop):
        mid = (start+stop)//2 
        # Recurse on the Left part
        L = maxSubArrayRecursive(arr, start, mid)
        # Recurse on the Right part
        R = maxSubArrayRecursive(arr, mid+1, stop)
        # Find the max crossing sum w.r.t. middle index
        C = maxCrossingSum(arr, start, mid, stop)
        return max(C, max(L,R)) 
    
    else:
        return arr[start]

def maxSubArray(arr):
    start = 0
    stop = len(arr) -1
    return maxSubArrayRecursive(arr, start, stop)

arr = [-2, 7, -6, 3, 1, -4, 5, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 13

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 6

arr = [-4, 14, -6, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 15

arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 10

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 7

