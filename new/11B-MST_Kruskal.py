import networkx as nx

# Create a graph instance
G = nx.Graph()

# Add edges and their weights to the graph
edges = [('A', 'C', 3), ('A', 'B', 5), ('B', 'C', 4), ('B', 'D', 6), ('C', 'D', 5),('B', 'E', 2), ('C', 'F', 6), ('D', 'E', 6), ('D', 'F', 6), ('E', 'F', 3), ('E', 'G', 4), ('G', 'F', 4)]
G.add_weighted_edges_from(edges)

# Compute the Minimum Spanning Tree using Kruskal's algorithm
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Print the constructed MST
print("Constructed MST:")
for edge in mst.edges(data=True):
    print(f"({edge[0]}) -- {edge[2]['weight']} -- ({edge[1]})")

# Calculate the total cost of the MST
total_cost = sum(edge[2]['weight'] for edge in mst.edges(data=True))
print(f"Total cost: {total_cost}")
