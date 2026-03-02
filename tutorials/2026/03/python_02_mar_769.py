class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to perform BFS traversal
    def BFS(self, start_vertex):
        visited = [False] * (self.V)
        distance = [0] * (self.V)
        queue = []

        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)

        # Perform BFS
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            # Visit all adjacent vertices
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[vertex] + 1
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)

    print("BFS Traversal:")
    g.BFS(0)