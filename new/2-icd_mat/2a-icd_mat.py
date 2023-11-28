class UndirectedGraphIncidenceMatrix:
    def __init__(self):
        self.node_indices = {}  # Maps node data to node index
        self.edges = []  # Stores pairs of node indices that represent edges
        self.inc_matrix = []  # Incidence matrix

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.node_indices:
            self.node_indices[node] = len(self.node_indices)
            # Initialize the new row with zeros for existing edges
            self.inc_matrix.append([0] * len(self.edges))

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2."""
        if node1 not in self.node_indices or node2 not in self.node_indices:
            raise ValueError("Both nodes must exist in the graph.")

        # Add a new column to represent this edge in the incidence matrix
        edge_index = len(self.edges)
        for row in self.inc_matrix:
            row.append(0)  # Start with 0 for all nodes

        # Update the incidence matrix for both nodes
        self.inc_matrix[self.node_indices[node1]][edge_index] = 1
        self.inc_matrix[self.node_indices[node2]][edge_index] = 1
        # Record the new edge
        self.edges.append((self.node_indices[node1], self.node_indices[node2]))

    def __str__(self):
        """String representation of the graph's incidence matrix."""
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.inc_matrix])
        return f"Incidence Matrix:\n{matrix_str}"


if __name__ == "__main__":
    # Usage Examples
    u_graph = UndirectedGraphIncidenceMatrix()
    u_graph.add_node("A")
    u_graph.add_node("B")
    u_graph.add_node(1)
    u_graph.add_node(2)

    u_graph.add_edge("A", "B")
    u_graph.add_edge("A", 1)
    u_graph.add_edge("A", 2)

    print(u_graph)
