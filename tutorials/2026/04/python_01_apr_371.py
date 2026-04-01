# Merge Sort Implementation in Python
```python
def merge_sort(arr):
    # Base case: If the array has 1 or fewer elements, return it as it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Find the middle point of the array to divide it into two halves.
    mid = len(arr) // 2
    
    # Divide the array into left and right halves.
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively call merge_sort on both halves until each subarray has one element.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted left and right halves into a single, sorted array.
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []
    
    # Initialize indices for both input lists.
    left_index = 0
    right_index = 0
    
    # Merge smaller elements first while keeping track of remaining elements in both lists.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # If there are remaining elements in either list, append them to the merged result.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged


# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)