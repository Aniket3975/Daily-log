# Dijkstra's Shortest Path Algorithm

```python
import sys
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm.

    Args:
    graph (dict): A dictionary representing the graph, where each key is a node and its value is a dictionary of neighboring nodes and their edge weights.
    start (node): The starting node for the shortest path algorithm.

    Returns:
    distances (dict): A dictionary containing the shortest distance from the start node to each node in the graph.
    previous (dict): A dictionary containing the previous node in the shortest path from the start node to each node.
    """
    # Initialize the distances and previous dictionaries
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # Create a priority queue to store nodes to be processed
    priority_queue = [(0, start)]

    while priority_queue:
        # Extract the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the already known distance, skip this node
        if current_distance > distances[current_node]:
            continue

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = current_distance + weight

            # If this distance is less than the already known distance, update the distance and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, previous = dijkstra(graph, start_node)

print("Shortest distances from", start_node, ":")
for node, distance in distances.items():
    print(node, ":", distance)

print("\nPrevious nodes in the shortest path:")
for node, previous_node in previous.items():
    print(node, ":", previous_node)