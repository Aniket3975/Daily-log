# Segment Tree implementation in Python

# Define a class to represent the segment tree
class SegmentTree:
    def __init__(self, arr):
        # Initialize the segment tree with the input array
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    # Function to build the segment tree
    def build_tree(self, arr, node, start, end):
        # If the current node is a leaf node, store the value from the array
        if start == end:
            self.tree[node] = arr[start]
        else:
            # Calculate the midpoint of the current node's range
            mid = (start + end) // 2
            # Recursively build the left and right subtrees
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            # Update the value of the current node with the minimum of its subtrees
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    # Function to update a value in the segment tree
    def update(self, index, value):
        # Calculate the node at which to update the value
        node = self.n + index
        # Update the value at the current node
        self.tree[node] = value
        # Update the values of the ancestors of the current node
        while node > 0:
            node = (node - 1) // 2
            # Update the value of the current node with the minimum of its subtrees
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    # Function to query the value at a given range
    def query(self, start, end):
        # Calculate the nodes at which to query the values
        node = self.n + start
        # Query the values of the ancestors of the current node
        left = self.tree[node]
        node = (node - 1) // 2
        while node > 0:
            if start <= self.tree[2 * node + 1] <= end:
                left = min(left, self.tree[2 * node + 1])
            elif self.tree[2 * node + 2] <= end:
                left = min(left, self.tree[2 * node + 2])
            node = (node - 1) // 2
        return left

# Run the example
arr = [1, 3, 5, 2, 4, 6, 7, 8, 9]
segment_tree = SegmentTree(arr)
print("Minimum value in the array:", segment_tree.query(0, len(arr) - 1))
segment_tree.update(3, 10)
print("Minimum value in the updated array:", segment_tree.query(0, len(arr) - 1))