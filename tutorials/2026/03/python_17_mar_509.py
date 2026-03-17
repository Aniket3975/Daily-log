# Sliding Window Technique in Python
=====================================

## Overview

The sliding window technique is a popular algorithmic approach used to solve problems that involve traversing and processing elements within a larger dataset. It's particularly useful when the problem has constraints on the size of the window or the order in which elements are processed.

## Problem Statement

Given an array of integers `arr` and a target integer `target`, find two elements in the array whose sum is equal to `target`.

## Solution
```python
def two_sum(arr, target):
    """
    Returns two indices into the array that add up to the target value.
    
    :param arr: List of integers
    :param target: Target sum
    :return: Indices of two elements in the array whose sum is equal to the target
    """
    # Create a dictionary to store the elements we've seen so far and their indices
    seen = {}
    
    # Iterate over the array with the index and value
    for i, num in enumerate(arr):
        # Calculate the complement of the current number (target - num)
        complement = target - num
        
        # Check if the complement is in the dictionary
        if complement in seen:
            # If it is, return the indices of the current number and its complement
            return [seen[complement], i]
        
        # If not, add the current number and its index to the dictionary
        seen[num] = i
    
    # If no solution is found after iterating over the entire array, return None
    return None

# Example usage:
arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))  # Output: [0, 1]

arr = [3, 2, 4]
target = 6
print(two_sum(arr, target))  # Output: [1, 2]

arr = [3, 3]
target = 6
print(two_sum(arr, target))  # Output: [0, 1]