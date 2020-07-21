# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) == 1 and arr[0] != target:
        return -1
    med = (start + end) // 2
    if arr[med] == target:
        return med
    if target > arr[med]:
        return binary_search(arr, target, med+1, len(arr)-1)
    if target < arr[med]:
        return binary_search(arr, target, 0, med-1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

