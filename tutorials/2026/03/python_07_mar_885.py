# prefix_sum.py

# The prefix sum technique is used to solve problems that require accessing elements from an array
# without having to read the entire array. This is particularly useful when solving problems
# where we need to keep track of the sum of elements up to a certain point.

def prefix_sum(arr):
    # Initialize an empty list to store the prefix sums.
    prefix_sums = [0] * (len(arr) + 1)
    
    # Iterate over the array and calculate the prefix sums.
    for i in range(len(arr)):
        # For each element, add the value of that element to the prefix sum
        # at the current index in the prefix_sums list.
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
        
    # Return the prefix sums list.
    return prefix_sums

def query_prefix_sum(prefix_sums, left, right):
    # If the left pointer is greater than the right pointer, return 0.
    # This is because we don't need to consider any elements
    # when the left pointer is greater than the right pointer.
    if left > right:
        return 0
    
    # Calculate the sum of elements from the left pointer to the right
    # pointer by subtracting the prefix sum at the left pointer from
    # the prefix sum at the right pointer plus 1.
    return prefix_sums[right + 1] - prefix_sums[left]

# Example usage:
arr = [1, 2, 3, 4, 5]
prefix_sums = prefix_sum(arr)
print("Prefix Sums:", prefix_sums)

# Example query:
left, right = 1, 3
result = query_prefix_sum(prefix_sums, left, right)
print("Sum from index", left, "to", right, "is", result)