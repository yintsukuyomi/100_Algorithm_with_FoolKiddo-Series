import heapq

def dijkstra(graph, start):
    # Distance to each node (default to infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to start node is 0

    # Priority queue to get the node with the smallest distance
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Sample graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Entry point
if __name__ == "__main__":
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest paths from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"  {start_node} → {node} = {distance}")