import random

# Header comment explaining what this teaches and why it is useful
"""
This script teaches about prefix sum arrays, a crucial data structure in algorithms.
A prefix sum array is an array where each element at index i stores the cumulative sum of all elements up to i.
It's useful for solving problems like finding the sum of all elements in a range or calculating the prefix sum efficiently.

The logic behind this script is based on iterating through the array and adding each new element to the previous sum.
This approach allows us to calculate the sum of any subarray in O(1) time, making it an efficient data structure for many applications.
"""

def initialize_prefix_sum_array(arr):
    """
    Initialize a prefix sum array by calculating the cumulative sum at each index.
    
    :param arr: The input array
    :return: A list representing the prefix sum array
    """
    # Create a new list to store the prefix sums, with the same length as the input array
    prefix_sums = [0] * len(arr)
    # The first element in the prefix sum array is always equal to the first element in the input array
    prefix_sums[0] = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Calculate the cumulative sum by adding the current element to the previous sum
        prefix_sums[i] = arr[i] + prefix_sums[i-1]
    
    return prefix_sums

def get_prefix_sum(prefix_sum_array, start, end):
    """
    Get the sum of a range in the original array using the prefix sum array.
    
    :param prefix_sum_array: The prefix sum array
    :param start: The starting index of the range (inclusive)
    :param end: The ending index of the range (inclusive)
    :return: The sum of the elements in the specified range
    """
    # Calculate the sum by subtracting the prefix sum at the start index from the prefix sum at the end index
    return prefix_sum_array[end] - prefix_sum_array[start-1]

# Generate a random array for testing
random_array = [random.randint(0, 100) for _ in range(10)]
print("Random Array:", random_array)

# Initialize the prefix sum array
prefix_sum_array = initialize_prefix_sum_array(random_array)
print("Prefix Sum Array:", prefix_sum_array)

# Test the function to get the sum of a range
start_index = 3
end_index = 6
result = get_prefix_sum(prefix_sum_array, start_index, end_index)
print(f"Sum from index {start_index} to {end_index}: {result}")