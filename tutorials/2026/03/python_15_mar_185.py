# Binary Search in Python
=====================================

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

```python
def binary_search(arr, target):
    # Initialize two pointers, low and high, to the start and end of the array
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        # If the target is at the middle index, return it
        if arr[mid] == target:
            return mid
        
        # If the target is less than the middle element, move to the left half
        elif arr[mid] > target:
            high = mid - 1
        
        # If the target is greater than the middle element, move to the right half
        else:
            low = mid + 1

    # If we've reached this point, the target wasn't in the array
    return None


# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 12
index = binary_search(arr, target)

if index is not None:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found in array")