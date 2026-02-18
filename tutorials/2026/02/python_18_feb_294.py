# Sliding Window Algorithm Implementation in Python

def max_sum_subarray(arr, k):
    """
    This function calculates the maximum sum of a subarray with size k.
    
    Parameters:
    arr (list): The input array.
    k (int): The size of the sliding window.

    Returns:
    int: The maximum sum of a subarray with size k.
    """

    # Initialize the window sum and its maximum value
    window_sum = 0
    max_window_sum = float('-inf')

    # Initialize the window boundaries
    left = 0

    # Iterate over the array with the right boundary of the window
    for right in range(len(arr)):
        # Add the current element to the window sum
        window_sum += arr[right]

        # If the window size is greater than k, remove the leftmost element from the window sum
        if right >= k - 1:
            max_window_sum = max(max_window_sum, window_sum)
            window_sum -= arr[left]
            left += 1

    return max_window_sum


# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
print("Maximum sum of a subarray with size", k, "is:", max_sum_subarray(arr, k))