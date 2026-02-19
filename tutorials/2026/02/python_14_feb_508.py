# Merge Sort Implementation in Python
=====================================================

This code teaches a fundamental sorting algorithm, Merge Sort, which is useful for efficient sorting of large datasets.

Merge Sort is a divide-and-conquer algorithm that works by dividing the input array into two halves, recursively sorting each half, and then merging the sorted halves back together.

```python
def merge_sort(arr):
    # Base case: If the length of the array is 1 or less, return the array (since it's already sorted)
    if len(arr) <= 1:
        return arr

    # Find the middle index to divide the array into two halves
    mid = len(arr) // 2

    # Recursively call merge_sort on each half of the array
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []

    # While there are still elements in both lists
    while len(left) > 0 and len(right) > 0:
        # Compare the smallest unmerged element from each list
        if left[0] <= right[0]:
            # Append the smaller element to the merged list
            merged.append(left.pop(0))
        else:
            # Append the larger element to the merged list
            merged.append(right.pop(0))

    # If there are remaining elements in either list, append them to the merged list
    merged.extend(left)
    merged.extend(right)

    return merged


# Example usage and test
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

    # Test case: Checking if the original array was sorted correctly
    for i in range(len(sorted_arr) - 1):
        assert sorted_arr[i] <= sorted_arr[i + 1], "Original array not sorted correctly"