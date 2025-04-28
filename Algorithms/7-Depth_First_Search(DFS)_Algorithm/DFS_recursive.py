def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
        
    return visited

#sample graph represented as adjaceny list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'Z'],
    'F': [],
    'Z': []
}

# Entry Point
if __name__ == "__main__" :
    print("Depth First Search starting from node A:")
    dfs(graph, 'A')