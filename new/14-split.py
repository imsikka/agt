def is_split_graph(graph):
    n = len(graph)  # Number of vertices
    degrees = sorted(
        ((v, sum(adj)) for v, adj in enumerate(graph)), key=lambda x: -x[1]
    )

    # Try to find the size of the maximum clique
    clique_size = 0
    for i, (v, degree) in enumerate(degrees):
        if degree < i:
            break
        clique_size += 1

    # Check if the first clique_size vertices form a clique
    for i in range(clique_size):
        for j in range(i + 1, clique_size):
            if not graph[degrees[i][0]][degrees[j][0]]:
                return False  # Not a clique

    # Check if the rest of the vertices form an independent set
    for i in range(clique_size, n):
        for j in range(i + 1, n):
            if graph[degrees[i][0]][degrees[j][0]]:
                return False  # Not an independent set

    return True


# Example usage:
# The adjacency matrix of the graph
# Vertices {0, 1, 2} form a clique and {3, 4} form an independent set
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

print(is_split_graph(graph))
