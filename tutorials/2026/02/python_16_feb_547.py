# Merge Sort Implementation in Python
======================================

This code teaches how to implement the merge sort algorithm, a popular sorting technique used for large datasets.

Merge sort is a divide-and-conquer algorithm that works by splitting an array into two halves until each half contains one element (a leaf node), and then merging these nodes back together in sorted order. This approach has a time complexity of O(n log n) on average, making it suitable for large datasets.

Here's the implementation:

```python
def merge_sort(arr):
    # Base case: if the array has only one element or is empty, return it as it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array into two halves
    mid = len(arr) // 2

    # Recursively sort each half of the array
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves back together in sorted order
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []
    left_index = 0
    right_index = 0

    # Compare elements from both lists and append the smaller one to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from either list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage and test
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

    # Test case: check if the sorted array is correct
    assert sorted(arr) == sorted(sorted_arr), "Merge sort algorithm failed"