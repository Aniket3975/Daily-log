# Union-Find Algorithm Implementation in Python

class UnionFind:
    def __init__(self, size):
        # Initialize the parent array with indices of each element
        self.parent = list(range(size))
        # Initialize the rank array with 0 for each element
        self.rank = [0] * size

    def find(self, x):
        # If the parent of x is not itself, find its root and update parent if necessary
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        # If they are not the same group, merge them
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                # If ranks are equal, make one the parent and increment its rank
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        # Check if elements belong to the same group
        return self.find(x) == self.find(y)

# Example usage:
if __name__ == "__main__":
    uf = UnionFind(5)
    
    # Add initial groups
    for i in range(3):
        uf.union(i, 3 + i)
    for j in range(2):
        uf.union(j * 3, (j + 1) * 3)

    print("Test 1: Elements within the same group")
    assert uf.connected(0, 1) == False
    assert uf.connected(1, 2) == False
    assert uf.connected(2, 3) == True

    # Test another scenario with different sizes
    uf = UnionFind(8)
    
    # Add initial groups
    for i in range(4):
        uf.union(i, 4 + i)

    print("Test 2: Different group sizes")
    assert uf.connected(0, 1) == False
    assert uf.connected(1, 2) == False
    assert uf.connected(2, 3) == True
    assert uf.connected(4, 5) == False
    assert uf.connected(5, 6) == False
    assert uf.connected(6, 7) == True