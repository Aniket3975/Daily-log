# Two Pointers Technique in Python
=====================================

The two pointers technique is an efficient way to solve problems involving arrays or linked lists where we need to find a specific element or complete a task.

```python
def remove_duplicates(nums):
    # If the input list has less than 2 elements, it's impossible to have duplicates
    if len(nums) < 2:
        return nums

    # Initialize two pointers: one at the beginning and one at the second element
    i = 0
    j = 1

    # Move the 'j' pointer until we find a unique element or reach the end of the list
    while j < len(nums):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        j += 1

    # Return the modified list, excluding duplicates
    return nums[:i+1]

# Example usage:
numbers = [1, 1, 2, 3, 4, 5, 5, 6]
print("Original List:", numbers)
print("List without Duplicates:", remove_duplicates(numbers))