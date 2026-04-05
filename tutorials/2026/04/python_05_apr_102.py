def find_max_value(arr):
    # Sort the array in decreasing order to consider largest values first
    arr.sort(reverse=True)
    
    # Initialize max_sum as the value of the first element in the sorted array
    max_sum = arr[0]
    
    # Iterate through the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Check if adding the current element to the sum exceeds the sum of its neighbors
        if arr[i] < (arr[i-1] + arr[i+1]):
            # If it does, add the current element to the max_sum and swap it with the next element in the array
            max_sum += arr[i]
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return max_sum

# Test the function with an example array
arr = [10, 7, 8, 9, 4, 5, 6]
print("Original Array:", arr)
print("Maximum possible sum of intervals:", find_max_value(arr))