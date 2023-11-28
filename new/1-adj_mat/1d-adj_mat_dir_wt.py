class DirectedWeightedGraph:
    def __init__(self):
        self.node_indices = {}  # Maps nodes (of any type) to their respective indices
        self.adj_matrix = []  # The adjacency matrix initialized as an empty list

    def add_node(self, node):
        """Add a new node to the graph if it doesn't already exist."""
        if node not in self.node_indices:
            # Assign an index to the new node
            self.node_indices[node] = len(self.node_indices)
            # Extend existing rows to include the new node
            for row in self.adj_matrix:
                row.append(
                    float('inf')
                )  # Use float('inf') for the absence of edges
            # Add a new row for the new node
            self.adj_matrix.append([float('inf')] * (len(self.node_indices)))

    def add_edge(self, from_node, to_node, weight):
        """Add a directed edge from from_node to to_node with the specified weight."""
        if from_node not in self.node_indices or to_node not in self.node_indices:
            raise ValueError("Both nodes must exist in the graph.")
        # Set the weight for the directed edge
        self.adj_matrix[self.node_indices[from_node]][
            self.node_indices[to_node]
        ] = weight

    def remove_edge(self, from_node, to_node):
        """Remove the directed edge from from_node to to_node."""
        if from_node in self.node_indices and to_node in self.node_indices:
            # Indicate the absence of an edge
            self.adj_matrix[self.node_indices[from_node]][
                self.node_indices[to_node]
            ] = float('inf')

    def get_edge_weight(self, from_node, to_node):
        """Get the weight of the edge from from_node to to_node."""
        if from_node in self.node_indices and to_node in self.node_indices:
            return self.adj_matrix[self.node_indices[from_node]][
                self.node_indices[to_node]
            ]
        return None

    def __str__(self):
        """String representation of the graph's adjacency matrix."""
        matrix_lines = ["\t".join(map(str, row)) for row in self.adj_matrix]
        matrix_str = "\n".join(matrix_lines)
        return f"Adjacency Matrix:\n{matrix_str}"


if __name__ == "__main__":
    # Usage Examples
    dwg = DirectedWeightedGraph()
    dwg.add_node("A")
    dwg.add_node("B")
    dwg.add_node("C")

    dwg.add_edge("A", "B", 4)
    dwg.add_edge("B", "C", 3)
    dwg.add_edge("A", "C", 10)

    print(dwg)
    print("Weight of the edge from 'A' to 'B':", dwg.get_edge_weight("A", "B"))
    print("Weight of the edge from 'B' to 'C':", dwg.get_edge_weight("B", "C"))
    print(
        "Weight of the edge from 'C' to 'A':", dwg.get_edge_weight("C", "A")
    )  # Should be None as it's not set

    dwg.remove_edge("A", "C")
    print("\nAfter removing the edge from 'A' to 'C':")
    print(dwg)
