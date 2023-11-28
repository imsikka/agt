import networkx as nx

# Create a graph instance
G = nx.Graph()

# Add edges to the graph
edges = [(0, 1), (0, 2), (0, 3),    (1, 2), (1, 3),    (2, 3),    (3, 4), (3, 5),    (4, 5)]
G.add_edges_from(edges)

# Check if the graph is triangulated (chordal)
is_triangulated = nx.is_chordal(G)

if is_triangulated:
    print("The graph is triangulated.")
else:
    print("The graph is not triangulated.")
