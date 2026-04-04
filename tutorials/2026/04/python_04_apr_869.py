# Divide and Conquer Algorithm
# ===========================

## Introduction

Divide and Conquer is an algorithmic technique used to solve complex problems by breaking them down into smaller sub-problems, solving each recursively, and then combining the solutions.

## Example Problem: Merge Sort

Merge sort is a popular sorting algorithm that uses divide and conquer. Here's a Python implementation of merge sort:

```python
def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array into two halves.
    mid = len(arr) // 2

    # Recursively call merge_sort on the left and right halves.
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted left and right halves.
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result.
    merged = []

    # Compare elements from both lists and add the smaller one to the merged list.
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Append any remaining elements from both lists.
    merged.extend(left)
    merged.extend(right)

    return merged


# Test the merge_sort function with a sample array.
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)