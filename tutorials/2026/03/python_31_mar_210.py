# Topological Sort in Python
#================================

import collections

def topological_sort(graph):
    """
    Performs a topological sort on the given graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
               Each key is a node, and its corresponding value is a set of nodes
               that it has an edge to.

    Returns:
        A list of nodes in topological order. If there's no valid order,
        raises ValueError.
    """
    # Initialize a dictionary to store the in-degree of each node
    in_degree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Initialize a queue with nodes having an in-degree of 0
    queue = [node for node, degree in in_degree.items() if degree == 0]

    # Initialize an empty list to store the sorted nodes
    sorted_nodes = []

    while queue:
        # Dequeue a node and add it to the sorted list
        node = queue.pop(0)
        sorted_nodes.append(node)

        # Decrease the in-degree of its neighbors by 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            # If the in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If there are remaining nodes with non-zero in-degree,
    # then there's a cycle and we can't perform topological sort
    if len(sorted_nodes) != len(graph):
        raise ValueError("Graph contains a cycle")

    return sorted_nodes

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'D', 'E'},
        'C': {'F'},
        'D': set(),
        'E': {'F'},
        'F': set()
    }

    try:
        sorted_nodes = topological_sort(graph)
        print("Topologically Sorted Nodes:", sorted_nodes)
    except ValueError as e:
        print(e)