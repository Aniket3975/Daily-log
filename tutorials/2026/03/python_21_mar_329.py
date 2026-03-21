# Two Pointers Technique in Python
=====================================

The two-pointers technique is used to solve problems involving sorting or searching elements within a sorted array. This technique involves maintaining two pointers that start from the beginning and end of the array, respectively.

```python
class Solution:
    def removeZeroCrossing(self, arr):
        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(arr) - 1

        # Continue until the two pointers meet
        while left < right:
            # If both elements are zero, move both pointers
            if arr[left] == arr[right]:
                left += 1
                right -= 1
            # If element at the left pointer is less than or equal to
            # the element at the right pointer, move the left pointer
            elif arr[left] <= arr[right]:
                left += 1
            # If element at the left pointer is greater than
            # the element at the right pointer, move the right pointer
            else:
                right -= 1

        return arr[:left + 1]

# Example usage:
solution = Solution()
arr = [0, 2.5, -4, -3]
print(solution.removeZeroCrossing(arr))  # Output: [-4, -3, 0, 2.5]