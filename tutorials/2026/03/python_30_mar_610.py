# Breadth First Search (BFS) Graph Traversal in Python
```python
from collections import deque

class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the given number of vertices
        self.V = vertices
        # Create an adjacency list to represent the graph
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add a directed edge from vertex u to vertex v
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        # Perform BFS traversal starting from the given vertex
        visited = [False] * (self.V + 1)
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            # Dequeue a vertex and visit it
            vertex = queue.popleft()
            print(vertex, end=" ")

            # Enqueue all unvisited adjacent vertices
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Create a sample graph with 5 vertices
g1 = Graph(5)

# Add edges to the graph
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 4)

print("BFS Traversal:")
g1.bfs(0)  # Start traversal from vertex 0

# Create another sample graph with 6 vertices
g2 = Graph(6)

# Add edges to the graph
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(1, 3)
g2.add_edge(1, 4)
g2.add_edge(2, 5)

print("\nBFS Traversal:")
g2.bfs(0)  # Start traversal from vertex 0