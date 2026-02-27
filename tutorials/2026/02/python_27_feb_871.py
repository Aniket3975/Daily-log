# Heap Operations in Python

# Import the required modules
import heapq

# Create a min heap
def create_min_heap():
    # Initialize an empty list to simulate a heap
    heap = []
    # Add elements to the heap
    heap.append(10)
    heap.append(20)
    heap.append(5)
    heap.append(15)
    heap.append(8)
    # Heapify the list to create a min heap
    heapq.heapify(heap)
    return heap

# Create a max heap
def create_max_heap():
    # Initialize an empty list to simulate a heap
    heap = []
    # Add elements to the heap
    heap.append(10)
    heap.append(20)
    heap.append(5)
    heap.append(15)
    heap.append(8)
    # Convert the list to a max heap by negating all elements
    heap = [-x for x in heap]
    # Heapify the list to create a max heap
    heapq.heapify(heap)
    return heap

# Heapify a list
def heapify_list(lst):
    # Initialize the heap size
    n = len(lst)
    # Start from the last non-leaf node
    i = n // 2 - 1
    # Heapify the list
    while i >= 0:
        # Heapify the sub-tree rooted at i
        heapify_sub_tree(lst, i, n)
        i -= 1

# Heapify the sub-tree
def heapify_sub_tree(lst, i, n):
    # Initialize the largest element's index
    largest = i
    # Calculate the left and right child's indices
    left = 2 * i + 1
    right = 2 * i + 2
    # Check if the left child exists and is greater than the root
    if left < n and lst[left] > lst[largest]:
        largest = left
    # Check if the right child exists and is greater than the root
    if right < n and lst[right] > lst[largest]:
        largest = right
    # If the largest element is not the root, swap them
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        # Heapify the affected sub-tree
        heapify_sub_tree(lst, largest, n)

# Extract the minimum element from the heap
def extract_min(heap):
    # Return the minimum element
    return heapq.heappop(heap)

# Get the top element from the heap
def get_top_element(heap):
    # Return the top element
    return heap[0]

# Main function
def main():
    # Create a min heap
    min_heap = create_min_heap()
    print("Min Heap:", min_heap)
    # Create a max heap
    max_heap = create_max_heap()
    print("Max Heap:", max_heap)
    # Extract the minimum element from the min heap
    min_element = extract_min(min_heap)
    print("Extracted Min Element:", min_element)
    # Get the top element from the max heap
    top_element = get_top_element(max_heap)
    print("Top Element of Max Heap:", top_element)

# Run the main function
if __name__ == "__main__":
    main()