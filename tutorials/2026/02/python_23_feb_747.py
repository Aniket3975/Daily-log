# Breadth-First Search (BFS) Graph Traversal in Python
=====================================================

## Introduction

Breadth-First Search (BFS) is a graph traversal algorithm that explores all the nodes at the present depth prior to moving on to the nodes at the next depth level.

## Code

```python
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add an edge between two vertices
        self.adj_list[u].append(v)

    def bfs(self, start_vertex):
        # Perform BFS traversal
        visited = [False] * self.V
        distance = [0] * self.V
        parent = [None] * self.V
        queue = deque()

        queue.append(start_vertex)
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    distance[neighbor] = distance[vertex] + 1
                    parent[neighbor] = vertex

        # Print the shortest distance from the start vertex to all other vertices
        print("\nShortest Distance:")
        for i in range(self.V):
            print(f"{start_vertex} -> {i}: {distance[i]}")

        # Print the parent of each vertex
        print("\nParent of Each Vertex:")
        for i in range(self.V):
            print(f"{start_vertex} -> {i}: {parent[i]}")


# Create a sample graph
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 5)

# Perform BFS traversal
g.bfs(0)
```

## Explanation

1.  We define a `Graph` class to represent a graph with vertices and edges.
2.  The `add_edge` method is used to add an edge between two vertices.
3.  The `bfs` method performs the BFS traversal. It initializes three arrays: `visited`, `distance`, and `parent` to keep track of visited vertices, shortest distances, and parent vertices, respectively.
4.  It uses a queue to perform the BFS traversal. The starting vertex is added to the queue, and then we enter a loop where we dequeue a vertex, print it, and enqueue its unvisited neighbors.
5.  Once the BFS traversal is complete, we print the shortest distance from the start vertex to all other vertices and the parent of each vertex.

## Example Output