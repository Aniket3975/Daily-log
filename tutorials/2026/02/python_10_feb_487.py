class SegmentTree:
    def __init__(self, nums):
        # Calculate the size of the segment tree based on the input list
        self.size = len(nums)
        if self.size == 0:
            return None
        self.tree = [0] * (4 * self.size)

        # Initialize the segment tree with the input list
        self._build_tree(nums, 0, 0, self.size - 1)

    def _build_tree(self, nums, node, start, end):
        # If the current sub-tree is a leaf node, set its value to the corresponding element in the input list
        if start == end:
            self.tree[node] = nums[start]
        else:
            # Calculate the midpoint of the current range
            mid = (start + end) // 2

            # Recursively build the left and right subtrees
            self._build_tree(nums, 2 * node + 1, start, mid)
            self._build_tree(nums, 2 * node + 2, mid + 1, end)

            # Update the value of the current node based on the values of its children
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, start, end):
        # Initialize the result with infinity
        result = float('inf')

        # Call the _query function to find the minimum value in the specified range
        self._query(0, 0, self.size - 1, start, end, result)

        return result

    def _query(self, node, start, end, query_start, query_end, result):
        # If the current sub-tree is out of bounds or does not cover the query range, return infinity
        if start > query_end or end < query_start:
            return

        # If the entire query range falls within the current sub-tree, update the result
        if start >= query_start and end <= query_end:
            result = min(result, self.tree[node])

        # Recursively search in the left and right subtrees
        mid = (start + end) // 2
        if query_start <= mid:
            self._query(2 * node + 1, start, mid, query_start, query_end, result)
        if query_end > mid:
            self._query(2 * node + 2, mid + 1, end, query_start, query_end, result)


# Test the SegmentTree class
if __name__ == "__main__":
    nums = [10, 5, 8, 3, 7]
    st = SegmentTree(nums)

    # Query the minimum value in the range [0, 2)
    print(st.query(0, 2))  # Output: 3

    # Query the minimum value in the range [1, 4)
    print(st.query(1, 4))  # Output: 5