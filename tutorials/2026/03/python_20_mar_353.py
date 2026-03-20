# Union-Find Data Structure in Python
=====================================================

Union-find is a data structure that keeps track of a set of elements partitioned into a number of disjoint sets. It provides two main operations: union and find.

```python
class UnionFind:
    def __init__(self, size):
        """
        Initialize the union-find data structure with a given size.
        
        :param size: The number of elements in each set.
        """
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        """
        Find the representative element (root) of the set containing `x`.
        
        :param x: An element in the sets.
        :return: The representative element of the set containing `x`.
        """
        if self.parent[x] != x:
            # If `x` is not the root, recursively find its parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Merge the sets containing `x` and `y`.
        
        :param x: An element in one of the sets.
        :param y: An element in the other set.
        """
        # Find the roots of the sets containing `x` and `y`
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # If the sets are not already merged, merge them
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(5)
    print("Initial sets:")
    for i in range(5):
        print(f"Set {i}: [{uf.find(i)}]")

    # Merge some sets
    uf.union(0, 2)
    uf.union(1, 3)

    print("\nSets after merge:")
    for i in range(5):
        print(f"Set {i}: [{uf.find(i)}]")

    # Check that the sets have been merged correctly
    assert uf.find(0) == uf.find(2)
    assert uf.find(1) == uf.find(3)