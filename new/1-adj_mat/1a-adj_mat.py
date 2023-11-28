class Graph:
    def __init__(self):
        self.nodes = {}  # Maps nodes to their respective indices
        self.adj_matrix = []  # The adjacency matrix

    def add_node(self, node):
        """Add a new node to the graph"""
        if node not in self.nodes:
            self.nodes[node] = len(self.nodes)
            for row in self.adj_matrix:
                row.append(0)  # Add a new column for the node
            self.adj_matrix.append([0] * len(self.nodes))  # Add a new row for the node

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2"""
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must exist in the graph.")

        index1, index2 = self.nodes[node1], self.nodes[node2]
        self.adj_matrix[index1][index2] = 1  # Since the graph is undirected,
        self.adj_matrix[index2][index1] = 1  # set both pairs to 1.

    def has_edge(self, node1, node2):
        """Check if there is an edge between node1 and node2"""
        if node1 not in self.nodes or node2 not in self.nodes:
            return False

        index1, index2 = self.nodes[node1], self.nodes[node2]
        return self.adj_matrix[index1][index2] == 1

    def remove_edge(self, node1, node2):
        """Remove an edge between node1 and node2"""
        if self.has_edge(node1, node2):
            index1, index2 = self.nodes[node1], self.nodes[node2]
            self.adj_matrix[index1][index2] = 0
            self.adj_matrix[index2][index1] = 0

    def __str__(self):
        """String representation of the graph's adjacency matrix"""
        matrix = "\n".join([" ".join(map(str, row)) for row in self.adj_matrix])
        return f"Adjacency Matrix:\n{matrix}"


if __name__ == "__main__":
    # Usage Examples
    g = Graph()
    g.add_node(1)
    g.add_node("A")
    g.add_node("B")

    g.add_edge(1, "A")
    g.add_edge("A", "B")

    print(g)
    print("Does an edge exist between 1 and 'A'? ", g.has_edge(1, "A"))
    print("Does an edge exist between 'A' and 'B'? ", g.has_edge("A", "B"))
    print("Does an edge exist between 1 and 'B'? ", g.has_edge(1, "B"))

    g.remove_edge("A", "B")
    print("\nAfter removing the edge between 'A' and 'B':")
    print(g)
