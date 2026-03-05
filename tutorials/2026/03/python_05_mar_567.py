# Heap Operations in Python

# Importing the necessary library
import heapq

# Create a max heap using the heapify function
def create_max_heap(arr):
    # Use the heapify function to convert an array into a max heap
    heapq._heapify_max(arr)
    return arr

# Function to find the parent index of a given index
def find_parent_index(index):
    # Calculate the parent index using the formula (index - 1) // 2
    parent_index = (index - 1) // 2
    return parent_index

# Function to find the left child index of a given index
def find_left_child_index(index):
    # Calculate the left child index using the formula 2 * index + 1
    left_child_index = 2 * index + 1
    return left_child_index

# Function to find the right child index of a given index
def find_right_child_index(index):
    # Calculate the right child index using the formula 2 * index + 2
    right_child_index = 2 * index + 2
    return right_child_index

# Function to swap two elements in the heap
def swap_elements(index1, index2):
    # Swap the elements at the given indices
    arr[index1], arr[index2] = arr[index2], arr[index1]

# Function to heapify the array
def heapify(arr, index):
    # Initialize the largest as the root
    largest = index
    # Find the left child
    left_child_index = find_left_child_index(index)
    # Find the right child
    right_child_index = find_right_child_index(index)
    # If the left child exists and is greater than the root
    if left_child_index < len(arr) and arr[left_child_index] > arr[largest]:
        # Update the largest
        largest = left_child_index
    # If the right child exists and is greater than the root
    if right_child_index < len(arr) and arr[right_child_index] > arr[largest]:
        # Update the largest
        largest = right_child_index
    # If the largest is not the root
    if largest != index:
        # Swap the largest with the root
        swap_elements(index, largest)
        # Recursively heapify the affected sub-tree
        heapify(arr, largest)

# Function to extract the maximum element from the heap
def extract_max(arr):
    # Check if the heap is empty
    if len(arr) == 0:
        return None
    # If the heap has only one element
    if len(arr) == 1:
        # Return the only element in the heap
        return arr.pop()
    # Store the maximum element
    max_element = arr[0]
    # Replace the root with the last element in the heap
    arr[0] = arr.pop()
    # Heapify the reduced heap
    heapify(arr, 0)
    # Return the maximum element
    return max_element

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
# Create a max heap
arr = create_max_heap(arr)
print("Max heap:", arr)
# Extract the maximum element
max_element = extract_max(arr)
print("Maximum element:", max_element)
arr