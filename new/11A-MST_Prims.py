import networkx as nx

# Create a graph instance
G = nx.Graph()

# Add edges and their weights to the graph
edges = [('A', 'B', 3), ('A', 'C', 1), ('B', 'C', 2), ('B', 'D', 4), ('C', 'D', 5)]
G.add_weighted_edges_from(edges)

# Compute the Minimum Spanning Tree using Prim's algorithm
mst = nx.minimum_spanning_tree(G)

# Print the constructed MST
print("Constructed MST:")
for edge in mst.edges(data=True):
    print(f"({edge[0]}) -- {edge[2]['weight']} -- ({edge[1]})")

# Calculate the total cost of the MST
total_cost = sum(edge[2]['weight'] for edge in mst.edges(data=True))
print(f"Total cost: {total_cost}")
