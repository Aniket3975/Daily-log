# Segment Tree Implementation in Python

class SegmentTree:
    def __init__(self, arr):
        # Initialize the segment tree with the given array
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)

        # Build the segment tree using a recursive approach
        self._build_tree(1, 0, self.n - 1, arr)

    def _build_tree(self, node, start, end, arr):
        # Base case: if start and end are equal, set the node's value to the array value at that index
        if start == end:
            self.tree[node] = arr[start]
        else:
            # Calculate the middle index for this node
            mid = (start + end) // 2

            # Recursively build the left and right subtrees
            self._build_tree(2 * node, start, mid, arr)
            self._build_tree(2 * node + 1, mid + 1, end, arr)

            # Update this node's value using the values of its subtrees
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, start, end):
        # Query the segment tree for a range [start, end]
        return self._query(1, 0, self.n - 1, start, end)

    def _query(self, node, start, end, left, right):
        # Base case: if we're outside the query range or it's fully inside
        if left <= start and end <= right:
            return self.tree[node]
        elif right < start or left > end:
            return float('-inf')

        # Calculate the middle index for this node
        mid = (start + end) // 2

        # Recursively query the subtrees that overlap with the query range
        result = float('-inf')
        if left <= mid and right >= mid:
            result = max(result, self._query(2 * node, start, mid, left, right))
        elif left <= mid:
            result = max(result, self._query(2 * node, start, mid, left, right))
        if right > mid:
            result = max(result, self._query(2 * node + 1, mid + 1, end, left, right))

        return result

    def update(self, index, value):
        # Update the segment tree at a given index
        self.tree[1] = value
        self._update(1, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        # Base case: if we're outside the update range or it's fully inside
        if index <= start and end <= index:
            self.tree[node] = value
        elif right < start or left > end:
            return

        # Calculate the middle index for this node
        mid = (start + end) // 2

        # Recursively update the subtrees that overlap with the update range
        if index <= mid and right >= mid:
            self._update(2 * node, start, mid, index, value)
            self._update(2 * node + 1, mid + 1