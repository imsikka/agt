class DirectedGraph:
    def __init__(self):
        self.node_indices = {}  # Maps nodes to their respective indices
        self.adj_matrix = []  # The adjacency matrix

    def add_node(self, node):
        """Add a new node to the graph."""
        if node not in self.node_indices:
            self.node_indices[node] = len(self.node_indices)
            for row in self.adj_matrix:
                row.append(0)  # Append 0 to existing rows to represent no edge
            self.adj_matrix.append(
                [0] * len(self.node_indices)
            )  # Append a new row for the new node

    def add_edge(self, from_node, to_node):
        """Add a directed, unweighted edge from from_node to to_node."""
        if from_node not in self.node_indices or to_node not in self.node_indices:
            raise ValueError("Both nodes must exist in the graph.")

        self.adj_matrix[self.node_indices[from_node]][self.node_indices[to_node]] = 1

    def remove_edge(self, from_node, to_node):
        """Remove the directed edge from from_node to to_node."""
        if from_node in self.node_indices and to_node in self.node_indices:
            self.adj_matrix[self.node_indices[from_node]][
                self.node_indices[to_node]
            ] = 0

    def has_edge(self, from_node, to_node):
        """Check if there is a directed edge from from_node to to_node."""
        if from_node in self.node_indices and to_node in self.node_indices:
            return (
                self.adj_matrix[self.node_indices[from_node]][
                    self.node_indices[to_node]
                ]
                == 1
            )
        return False

    def __str__(self):
        """String representation of the graph's adjacency matrix."""
        matrix_lines = ["\t".join(map(str, row)) for row in self.adj_matrix]
        matrix_str = "\n".join(matrix_lines)
        return f"Adjacency Matrix:\n{matrix_str}"


if __name__ == "__main__":
    # Usage Examples
    dg = DirectedGraph()
    dg.add_node(1)
    dg.add_node("A")
    dg.add_node("B")

    dg.add_edge(1, "A")
    dg.add_edge("A", "B")

    print(dg)
    print("Is there an edge from 1 to 'A'? ", dg.has_edge(1, "A"))
    print("Is there an edge from 'A' to 1? ", dg.has_edge("A", 1))
    print("Is there an edge from 'A' to 'B'? ", dg.has_edge("A", "B"))

    dg.remove_edge("A", "B")
    print("\nAfter removing the edge from 'A' to 'B':")
    print(dg)
