def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            # Add neighbors in reverse order to simulate recursive DFS behavior
            stack.extend(reversed(graph[vertex]))

 # Define a sample graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#Entry point
if __name__ == "__main__":

    print("\nDepth First Search (Iterative) starting from node A:")
    dfs_iterative(graph, 'A')