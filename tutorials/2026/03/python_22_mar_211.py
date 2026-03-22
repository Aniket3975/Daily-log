# Binary Search Algorithm in Python

def binary_search(arr, target):
    """
    Searches for the target element in the sorted array using binary search algorithm.
    
    Args:
        arr (list): Sorted list of elements.
        target: Element to be searched in the array.
        
    Returns:
        int: Index of the target element if found; -1 otherwise.
    """

    # Initialize two pointers, low and high, to the start and end of the array
    low = 0
    high = len(arr) - 1

    # Continue searching while the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        
        # If the target element is found at the mid index, return the mid index
        if arr[mid] == target:
            return mid
        # If the target element is less than the middle element, move the high pointer to mid - 1
        elif arr[mid] > target:
            high = mid - 1
        # If the target element is greater than the middle element, move the low pointer to mid + 1
        else:
            low = mid + 1
    
    # If the target element is not found in the array, return -1
    return -1

# Example usage of binary search algorithm
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 6
    result = binary_search(arr, target)
    
    if result != -1:
        print("Element {} found at index {}".format(target, result))
    else:
        print("Element not found in the array")