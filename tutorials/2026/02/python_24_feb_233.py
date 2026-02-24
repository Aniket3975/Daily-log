# Heap Operations in Python

import heapq

def heapify(arr, n, i):
    """
    Heapify the array at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child is larger than the root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if the right child is larger than the root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If the largest is not the root, swap them and heapify the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert_heap(arr, k):
    """
    Insert an element into the heap.
    """
    arr[k] = arr[k].setdefault(0, 0) + 1
    heapq.heapify(arr)

def delete_min_heap(arr):
    """
    Delete the minimum element from the heap.
    """
    if len(arr) > 0:
        return heapq.heappop(arr)

def print_heap(arr):
    """
    Print the heap.
    """
    print("Heap: ", end='')
    for i in arr:
        print(i, end=' ')
    print()

def main():
    # Create an array
    arr = [12, 11, 13, 5, 6, 7]

    # Heapify the array
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("Initial heap: ")
    print_heap(arr)

    # Insert elements into the heap
    insert_heap(arr, 0)
    insert_heap(arr, 1)
    insert_heap(arr, 2)
    insert_heap(arr, 3)
    insert_heap(arr, 4)
    insert_heap(arr, 5)

    print("Heap after insertion: ")
    print_heap(arr)

    # Delete the minimum element from the heap
    min_element = delete_min_heap(arr)
    print("Deleted minimum element: ", min_element)

    print("Heap after deletion: ")
    print_heap(arr)

if __name__ == "__main__":
    main()