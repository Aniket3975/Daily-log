# Prefix Sum Algorithm in Python

# Define a function to calculate the prefix sum
def prefix_sum(arr):
    # Create a new list to store the prefix sum
    prefix = [0] * (len(arr) + 1)

    # Iterate over the array and calculate the prefix sum
    for i in range(len(arr)):
        # The prefix sum at index i is the sum of all elements up to i
        prefix[i + 1] = prefix[i] + arr[i]

    # Return the prefix sum array
    return prefix

# Define a function to query the prefix sum
def query_prefix_sum(prefix, left, right):
    # If left is greater than right, return 0
    if left > right:
        return 0

    # Calculate the prefix sum at index right + 1
    return prefix[right + 1] - prefix[left]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)

# Query the prefix sum
print(query_prefix_sum(prefix, 0, 2))  # Output: 3 (1 + 2)
print(query_prefix_sum(prefix, 1, 3))  # Output: 6 (2 + 3 + 4)
print(query_prefix_sum(prefix, 0, 4))  # Output: 10 (1 + 2 + 3 + 4 + 5)