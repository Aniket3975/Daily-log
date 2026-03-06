# Two Pointers Technique
=====================================

The two pointers technique is a common approach used in solving problems involving arrays, linked lists, or strings. It involves using two pointers, one that starts at the beginning of the array and another that starts at a specific position.

### Problem Statement

Given an array of integers, find the maximum sum of a subarray of size k.

### Solution

```python
def max_subarray_sum(arr, k):
    # Check if array is empty
    if not arr:
        return 0

    # Initialize two pointers
    left = 0
    right = 0

    # Initialize maximum sum
    max_sum = 0

    # Initialize current sum
    current_sum = 0

    # Initialize window size
    window_size = k

    # Iterate over the array
    while right < len(arr):
        # Add current element to current sum
        current_sum += arr[right]

        # If window size is reached, subtract leftmost element from current sum
        if right - left + 1 == window_size:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[left]
            left += 1

        # Move right pointer
        right += 1

    return max_sum

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
print(max_subarray_sum(arr, k))  # Output: 12