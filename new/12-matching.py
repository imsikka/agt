import networkx as nx

def compute_matching(graph):
    matching_edges = set()

    # Iterate over all edges in the graph
    for edge in graph.edges():
        u, v = edge

        # Check if the vertices are not incident to any edge in the matching
        if all(u not in edge and v not in edge for edge in matching_edges):
            matching_edges.add(edge)

    return matching_edges

# Create a graph instance
G = nx.Graph()

# Add edges to the graph
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
G.add_edges_from(edges)

# Compute the matching set of edges
matching_edges = compute_matching(G)

# Print the matching edges
print("Matching edges:", matching_edges)
