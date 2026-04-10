# Sliding Window in Python
=====================================

This script demonstrates the use of a sliding window technique to solve a common problem in algorithm design.

```python
def max_sum_subarray(nums, k):
    """
    Calculate the maximum sum of a subarray of size k.
    
    Args:
        nums (list): A list of integers.
        k (int): The size of the subarray.
        
    Returns:
        int: The maximum sum of a subarray of size k.
    """
    # Initialize the window start and end pointers
    left = 0
    
    # Calculate the initial sum of the first window
    current_sum = sum(nums[:k])
    
    # Store the maximum sum seen so far
    max_sum = current_sum
    
    # Slide the window to the right
    for right in range(k, len(nums)):
        # Subtract the element going out of the window and add the new element entering the window
        current_sum = current_sum - nums[left] + nums[right]
        
        # Update the maximum sum if necessary
        max_sum = max(max_sum, current_sum)
        
        # Move the window to the right by one step
        left += 1
    
    return max_sum

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 3
    
    result = max_sum_subarray(nums, k)
    print("Maximum sum of a subarray of size", k, "is:", result)