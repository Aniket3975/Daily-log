class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.tree = [0] * (4 * self.N)
        self.build_tree(arr, 0, 0, self.N - 1)

    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            return self.query(2 * node + 1, start, mid, left, right) + self.query(2 * node + 2, mid + 1, end, left, right)

    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    segment_tree = SegmentTree(arr)
    print("Sum of first three elements: ", segment_tree.query(0, 0, len(arr) - 1, 0, 2))
    print("Sum of last three elements: ", segment_tree.query(0, 0, len(arr) - 1, 6, 8))
    segment_tree.update(0, 0, len(arr) - 1, 5, 20)
    print("Sum of first five elements after update: ", segment_tree.query(0, 0, len(arr) - 1, 0, 4))


if __name__ == "__main__":
    main()