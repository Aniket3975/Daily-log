# Two Pointer Approach Explanation in Python

This script teaches the two pointer approach, a technique used to solve problems that involve arrays or linked lists. It's useful when we need to process elements from both ends of a data structure.

```python
def two_pointers(arr):
    """
    This function demonstrates the two-pointer approach using an array.
    
    Parameters:
    arr (list): The input array
    
    Returns:
    list: A new array with the desired result
    """
    
    # Initialize two pointers at the beginning and end of the array
    left = 0  # Left pointer starts from the first element of the array
    right = len(arr) - 1  # Right pointer starts from the last element of the array
    
    # Continue processing elements until the two pointers meet
    while left < right:
        # Process elements at the left and right pointers
        print(f"Processing {arr[left]} (left) and {arr[right]} (right)")
        
        # If we want to move the left pointer to the next element, do so
        if process_left(arr, left):
            left += 1
        
        # If we want to move the right pointer to the previous element, do so
        elif process_right(arr, right):
            right -= 1
    
    return arr


def process_left(arr, index):
    """
    This function decides whether to move the left pointer to the next element or not.
    
    Parameters:
    arr (list): The input array
    index (int): The current position of the left pointer
    
    Returns:
    bool: True if the left pointer should be moved to the next element, False otherwise
    """
    
    # For this example, let's say we want to move the left pointer to the next element when the value is greater than 5
    return arr[index] > 5


def process_right(arr, index):
    """
    This function decides whether to move the right pointer to the previous element or not.
    
    Parameters:
    arr (list): The input array
    index (int): The current position of the right pointer
    
    Returns:
    bool: True if the right pointer should be moved to the previous element, False otherwise
    """
    
    # For this example, let's say we want to move the right pointer to the previous element when the value is less than 3
    return arr[index] < 3


# Example usage and test
if __name__ == "__main__":
    # Create a sample array
    arr = [1, 2, 3, 4, 5]
    
    # Call the two_pointers function with the sample array
    new_arr = two_pointers(arr)
    
    # Print the result
    print(new_arr)