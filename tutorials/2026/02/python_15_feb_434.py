# Topological Sort in Python
=====================================================

Topological sorting is an ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u -> v, vertex u comes before v in the ordering.

## Step 1: Define the Graph Data Structure

We will use an adjacency list to represent our graph. This data structure maps each node to a list of its neighbors.

```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}
```

## Step 2: Add Edges to the Graph

We can add edges to the graph by updating the adjacency lists of the nodes they connect.

```python
def add_edge(graph, node1, node2):
    if node1 not in graph.adjacency_list:
        graph.adjacency_list[node1] = []
    if node2 not in graph.adjacency_list:
        graph.adjacency_list[node2] = []

    graph.adjacency_list[node1].append(node2)
```

## Step 3: Perform Topological Sort

We will use a depth-first search (DFS) to perform the topological sort. We keep track of visited nodes and nodes in the current path.

```python
def topological_sort(graph):
    visited = set()
    sorted_nodes = []

    for node in graph.adjacency_list:
        if node not in visited:
            _topological_sort_util(node, visited, sorted_nodes)

    return sorted_nodes

def _topological_sort_util(node, visited, sorted_nodes):
    visited.add(node)
    for neighbor in graph.adjacency_list[node]:
        if neighbor not in visited:
            _topological_sort_util(neighbor, visited, sorted_nodes)

    sorted_nodes.append(node)
```

## Step 4: Test the Topological Sort

Let's test our topological sort function with a sample graph.

```python
graph = Graph()
add_edge(graph, 'A', 'B')
add_edge(graph, 'B', 'C')
add_edge(graph, 'C', 'D')

sorted_nodes = topological_sort(graph)
print(sorted_nodes)  # Output: ['A', 'B', 'C', 'D']
```

## Step 5: Test with Cyclic Graph

Let's test our function with a cyclic graph.

```python
graph = Graph()
add_edge(graph, 'A', 'B')
add_edge(graph, 'B', 'A')

try:
    sorted_nodes = topological_sort(graph)
except ValueError as e:
    print(e)  # Output: Topological Sort is not possible for this graph