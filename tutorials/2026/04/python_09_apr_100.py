# Binary Search Algorithm Implementation in Python

def binary_search(arr, target):
    """
    Searches for a target element in a sorted array using binary search algorithm.

    Args:
        arr (list): A sorted list of elements.
        target: The target element to be searched.

    Returns:
        int: The index of the target element if found. -1 otherwise.
    """

    # Initialize two pointers, low and high, to represent the range of the array
    low = 0
    high = len(arr) - 1

    # Continue searching until the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the mid index to divide the search space in half
        mid = (low + high) // 2
        
        # Compare the target element with the middle element of the array
        if arr[mid] == target:
            return mid  # Return the index of the target element if found
            
        # If the target element is less than the middle element, update the high pointer
        elif target < arr[mid]:
            high = mid - 1
            
        # If the target element is greater than the middle element, update the low pointer
        else:
            low = mid + 1

    # Return -1 if the target element is not found in the array
    return -1


# Example usage of binary search function
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 8
    
    result = binary_search(arr, target)
    
    if result != -1:
        print("Target element found at index", result)
    else:
        print("Target element not found in the array")