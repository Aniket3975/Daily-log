class UnionFind:
    def __init__(self, n):
        # Initialize parent array for each node
        self.parent = list(range(n))
        
        # Initialize rank array for each node
        self.rank = [0] * n
    
    def find(self, x):
        # If x is not the root of itself, find its root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Find roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # If the two groups have the same root, then they are already connected
        if root_x != root_y:
            # Make one group the parent of the other
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                # If ranks are equal, make one group the parent of the other and increment its rank
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# Example usage:
if __name__ == "__main__":
    uf = UnionFind(6)

    # Step 1: Create a new union-find object with 6 nodes
    print("Step 1: Creating a new union-find object with 6 nodes")
    
    # Step 2: Find the root of node 0
    print("\nStep 2: Finding the root of node 0")
    print(uf.find(0))
    
    # Step 3: Union node 0 and node 1, find the new root
    uf.union(0, 1)
    print("New root after union:", uf.find(0))

    # Step 4: Find the roots of nodes 0 and 1
    print("\nStep 4: Finding the roots of nodes 0 and 1")
    print(uf.find(0), uf.find(1))
    
    # Step 5: Union node 2 and node 3, find the new root
    uf.union(2, 3)
    print("New root after union:", uf.find(2))

    # Step 6: Find the roots of nodes 0 and 2
    print("\nStep 6: Finding the roots of nodes 0 and 2")
    print(uf.find(0), uf.find(2))