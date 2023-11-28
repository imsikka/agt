class DirectedWeightedGraphIncidenceMatrix:
    def __init__(self):
        self.node_indices = {}  # Maps node data (Any type) to node index
        self.edges = []  # Stores tuples of node indices (origin, destination)
        self.inc_matrix = []  # Incidence matrix

    def add_node(self, node):
        """Add a node to the graph if it does not exist."""
        if node not in self.node_indices:
            self.node_indices[node] = len(self.node_indices)
            # Add a new row filled with float('inf') for existing edges
            self.inc_matrix.append([float("inf")] * len(self.edges))

    def add_edge(self, from_node, to_node, weight):
        """Add a directed edge from from_node to to_node with the specified weight."""
        if from_node not in self.node_indices or to_node not in self.node_indices:
            raise ValueError("Both nodes must exist in the graph.")

        # Add a new column for the new edge in the incidence matrix
        edge_index = len(self.edges)
        for row in self.inc_matrix:
            # Start with 0 for every node
            row.append(float("inf"))

        # For directed graphs, from_node has -weight and to_node has weight
        self.inc_matrix[self.node_indices[from_node]][edge_index] = -weight  # Outgoing
        self.inc_matrix[self.node_indices[to_node]][edge_index] = weight  # Incoming
        # Record the new edge
        self.edges.append(
            (self.node_indices[from_node], self.node_indices[to_node], weight)
        )

    def __str__(self):
        """Create a string representation of the incidence matrix."""
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.inc_matrix])
        return f"Incidence Matrix:\n{matrix_str}"


if __name__ == "__main__":
    # Usage examples
    digraph_weighted_inc = DirectedWeightedGraphIncidenceMatrix()
    digraph_weighted_inc.add_node("A")
    digraph_weighted_inc.add_node("B")
    digraph_weighted_inc.add_node(1)
    digraph_weighted_inc.add_node(2)

    digraph_weighted_inc.add_edge("A", "B", 3)
    digraph_weighted_inc.add_edge("A", 1, 5)
    digraph_weighted_inc.add_edge("A", 2, 6)

    print(digraph_weighted_inc)
