# Floyd-Warshall Algorithm to find all-pairs shortest paths
def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph] # Deep copy of graph matrix

    for k in range(V): # Intermediate vertices
        for i in range(V): # Source vertex
            for j in range(V): # Destination vertex
                if dist[i][k] + dist [k][j] < dist [i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example graph represented by an adjacency matrix
INF = float('inf')
graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

# Run the algorithm
result = floyd_warshall(graph)

# Print the result
print("All-Pairs Shortest Path Matrix:")
for row in result:
    print(row)