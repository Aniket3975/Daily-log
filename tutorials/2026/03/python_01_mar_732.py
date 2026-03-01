# Union-Find Algorithm Implementation in Python

```python
class UnionFind:
    def __init__(self, n):
        # Initialize a list to store the parent of each node
        self.parent = list(range(n))
        # Initialize a list to store the rank of each node
        self.rank = [0] * n

    def find(self, x):
        # If the node is the parent of itself, return it
        if self.parent[x] == x:
            return x
        # Otherwise, recursively find the root
        return self.find(self.parent[x])

    def union(self, x, y):
        # Find the roots of the two nodes
        root_x = self.find(x)
        root_y = self.find(y)
        # If the roots are different, merge the trees
        if root_x != root_y:
            # If the rank of root_x is less than root_y, make root_y the parent
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            # If the rank of root_x is greater than root_y, make root_x the parent
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            # If the ranks are equal, make root_x the parent and increment its rank
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# Example usage
if __name__ == "__main__":
    n = 5  # number of nodes
    uf = UnionFind(n)  # create an instance of UnionFind

    # Perform some union operations
    uf.union(0, 1)  # 0 and 1 are in the same group
    uf.union(1, 2)  # 1 and 2 are in the same group
    uf.union(3, 4)  # 3 and 4 are in the same group

    # Perform some find operations
    print(uf.find(0))  # 0 is in group 0
    print(uf.find(1))  # 1 is in group 0
    print(uf.find(2))  # 2 is in group 0
    print(uf.find(3))  # 3 is in group 3
    print(uf.find(4))  # 4 is in group 3