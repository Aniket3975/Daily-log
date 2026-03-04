# Heap Operations Example

# Importing the heapq module
import heapq

# Defining a heap
def define_heap():
    # Create a heap from a list
    heap = [10, 5, 20, 3, 7]
    heapq.heapify(heap)
    print("Initial Heap:", heap)

# Inserting elements into the heap
def insert_into_heap():
    # Create a new heap
    heap = []
    # Inserting elements into the heap
    for i in [1, 2, 3, 4, 5]:
        heapq.heappush(heap, i)
    print("Heap after Insertion:", heap)

# Removing elements from the heap
def remove_from_heap():
    # Create a new heap
    heap = []
    # Inserting elements into the heap
    for i in [1, 2, 3, 4, 5]:
        heapq.heappush(heap, i)
    print("Heap before Removal:", heap)
    # Removing the smallest element from the heap
    removed_element = heapq.heappop(heap)
    print("Removed Element:", removed_element)
    print("Heap after Removal:", heap)

# Heap operations
def heap_operations():
    # Create a new heap
    heap = []
    # Inserting elements into the heap
    for i in [1, 2, 3, 4, 5]:
        heapq.heappush(heap, i)
    print("Heap after Insertion:", heap)

    # Removing the smallest element from the heap
    removed_element = heapq.heappop(heap)
    print("Removed Element:", removed_element)
    print("Heap after Removal:", heap)

    # Inserting an element at the end of the heap
    heapq.heappush(heap, 6)
    print("Heap after Insertion:", heap)

    # Removing the smallest element from the heap
    removed_element = heapq.heappop(heap)
    print("Removed Element:", removed_element)
    print("Heap after Removal:", heap)

# Testing the heap operations
def test_heap_operations():
    define_heap()
    insert_into_heap()
    remove_from_heap()
    heap_operations()

# Running the test function
if __name__ == "__main__":
    test_heap_operations()