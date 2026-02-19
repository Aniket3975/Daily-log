# Merge Sort Implementation in Python
=====================================

This code teaches the concept of merge sort, a popular sorting algorithm that uses a divide-and-conquer approach to sort arrays of elements.

Merge sort is useful because it has a time complexity of O(n log n), making it efficient for large datasets. It's also relatively simple to implement and understand, making it a great choice for beginners and experts alike.

```python
def merge_sort(arr):
    # Base case: if the array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point of the array
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # While there are elements in both lists, compare and add the smaller one
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # If there are remaining elements in either list, append them to the merged result
    merged.extend(left)
    merged.extend(right)

    return merged


# Example usage and testing
if __name__ == "__main__":
    import random

    arr = [random.randint(1, 100) for _ in range(10)]
    print("Original array:", arr)

    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

    # Test the implementation with a small array
    small_arr = [3, 1, 4, 2]
    print("Small array:", small_arr)

    sorted_small_arr = merge_sort(small_arr)
    print("Sorted small array:", sorted_small_arr)