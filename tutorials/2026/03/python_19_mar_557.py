import heapq

# Initialize an empty heap
heap = []

# Push elements onto the heap
# We use the built-in heapq.heappush function to add elements to the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

# Pop elements from the heap
# The heappop function removes and returns the smallest element from the heap
print("Popped Element:", heapq.heappop(heap))

# Push another element onto the heap
heapq.heappush(heap, 15)

# Heapify a list to create a min-heap
# We use the built-in sorted function to sort the list in ascending order
my_list = [5, 2, 9, 1, 7]
sorted_list = sorted(my_list)
print("Sorted List:", sorted_list)

# Convert the sorted list back into a heap
# We use the heapq.heapify function to convert the list into a min-heap
heapq.heapify(sorted_list)
print("Heapified List:", sorted_list)

# Heap operations
def heap_operations(heap):
    # Get the size of the heap
    print("Size of Heap:", len(heap))
    
    # Get the smallest element from the heap
    print("Smallest Element:", min(heap))

    # Remove and return the smallest element from the heap
    print("Removed Element:", heapq.heappop(heap))

# Test the function with a sample heap
heap = [10, 5, 20]
heap_operations(heap)