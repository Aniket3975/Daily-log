# Sliding Window Technique in Python
=====================================

This script demonstrates the use of the sliding window technique to solve a common problem in algorithm design.

```python
def max_sum_subarray(arr, k):
    # Initialize variables to store maximum sum and current window sum
    max_sum = float('-inf')
    window_sum = 0
    
    # Calculate prefix sum for the first window
    for i in range(k):
        window_sum += arr[i]
        
    # Update maximum sum if the initial window sum is greater
    max_sum = max(window_sum, max_sum)
    
    # Slide the window to the right and update sums
    left = 0
    for right in range(k, len(arr)):
        # Remove element going out of the window from the current sum
        window_sum -= arr[left]
        left += 1
        
        # Add new element coming into the window to the current sum
        window_sum += arr[right]
        
        # Update maximum sum if the current window sum is greater
        max_sum = max(window_sum, max_sum)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum subarray of size", k, "is:", max_sum_subarray(arr, k))