# Monotonic Stack: A Data Structure for Efficient Binary Search
# This script teaches how to implement a monotonic stack in Python,
# which is useful when dealing with binary search and range queries.
# The monotonic stack data structure allows us to track all the elements 
# that can be considered as part of an increasing or decreasing subarray.

import bisect

class MonotonicStack:
    # Initialize the stack
    def __init__(self):
        self.stack = []

    # Push an element onto the stack
    def push(self, x):
        index = bisect.bisect_right(self.stack, x)
        self.stack.insert(index, x)

    # Pop the top element from the stack
    def pop(self):
        return self.stack.pop()

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0


# Example usage:
if __name__ == "__main__":
    # Create a monotonic stack for increasing order
    increasing_stack = MonotonicStack()
    increasing_stack.push(5)
    increasing_stack.push(10)
    increasing_stack.push(20)

    print("Increasing Stack:", increasing_stack.stack)  # Output: [5, 10, 20]

    # Pop the top element from the stack
    popped_element = increasing_stack.pop()
    print("Popped Element:", popped_element)  # Output: 20

    print("Increasing Stack after pop:", increasing_stack.stack)  # Output: [5, 10]

    # Create a monotonic stack for decreasing order
    decreasing_stack = MonotonicStack()
    decreasing_stack.push(5)
    decreasing_stack.push(10)
    decreasing_stack.push(20)

    print("Decreasing Stack:", decreasing_stack.stack)  # Output: [5, 10, 20]

    # Pop the top element from the stack
    popped_element = decreasing_stack.pop()
    print("Popped Element:", popped_element)  # Output: 20

    print("Decreasing Stack after pop:", decreasing_stack.stack)  # Output: [5, 10]