class WeightedGraphIncidenceMatrix:
    def __init__(self):
        self.node_indices = {}  # Maps node data to node index
        self.edges = (
            []
        )  # Stores tuples of (node index, node index, weight) that represent edges
        self.inc_matrix = []  # Incidence matrix

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.node_indices:
            self.node_indices[node] = len(self.node_indices)
            # Add a row filled with float('inf')
            self.inc_matrix.append([float("inf")] * len(self.edges))

    def add_edge(self, node1, node2, weight):
        """Add an edge between node1 and node2 with a given weight."""
        if node1 not in self.node_indices or node2 not in self.node_indices:
            raise ValueError("Both nodes must exist in the graph.")

        # Add a new column for the new edge in the incidence matrix
        edge_index = len(self.edges)
        for row in self.inc_matrix:
            # Nodes not connected by new edge have float('inf')
            row.append(float('inf'))  

        # Update the incidence matrix for the two endpoints of the edge
        self.inc_matrix[self.node_indices[node1]][edge_index] = weight
        self.inc_matrix[self.node_indices[node2]][edge_index] = weight
        # Record the new edge and its weight
        self.edges.append((self.node_indices[node1], self.node_indices[node2], weight))

    def __str__(self):
        """String representation of the graph's incidence matrix."""
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.inc_matrix])
        return f"Incidence Matrix:\n{matrix_str}"


# Usage Examples
w_graph = WeightedGraphIncidenceMatrix()
w_graph.add_node("A")
w_graph.add_node("B")
w_graph.add_node(1)
w_graph.add_node(2)

w_graph.add_edge("A", "B", 3)
w_graph.add_edge("A", 1, 5)
w_graph.add_edge("A", 2, 4)

print(w_graph)
