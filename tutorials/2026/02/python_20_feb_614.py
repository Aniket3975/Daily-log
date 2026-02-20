# Merge Sort Algorithm Implementation

def merge_sort(arr):
    # If the array has only one element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to divide the array into two halves
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty list to store the merged result
    merged = []
    left_index = 0
    right_index = 0

    # Merge smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either half, append them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Test the merge sort algorithm
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    print("Sorted array:", merge_sort(arr))