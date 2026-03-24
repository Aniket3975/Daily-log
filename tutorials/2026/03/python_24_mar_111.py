# Topological Sort in Python
=====================================

A topological sort is an ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    # function to add an edge
    def addEdge(self,u,v):
        self.graph[u].append(v)
            
    # function to find topological sort using DFS
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)

    # function to do topological sort
    def topologicalSort(self):
        visited = [False]*self.V
        stack = deque()
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
                
        return list(stack)


# Example usage:
if __name__ == "__main__":
    g1 = Graph(6);
    g1.addEdge(5, 2);
    g1.addEdge(5, 0);
    g1.addEdge(4, 0);
    g1.addEdge(4, 1);
    g1.addEdge(2, 3);
    g1.addEdge(3, 1);

    print("Topological Sort of the given graph is:");
    print(g1.topologicalSort())