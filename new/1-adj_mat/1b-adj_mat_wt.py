class WeightedGraph:
    def __init__(self):
        self.nodes = {}  # Maps nodes to indices
        self.adj_matrix = []  # The adjacency matrix

    def add_node(self, node):
        """Add a new node to the graph"""
        if node not in self.nodes:
            self.nodes[node] = len(self.nodes)
            for row in self.adj_matrix:
                # Use float('inf') for absent edges
                row.append(float("inf"))
            new_row = [float('inf')] * len(self.nodes)  # New row for the new node
            self.adj_matrix.append(new_row)

    def add_edge(self, node1, node2, weight):
        """Add an undirected, weighted edge between node1 and node2"""
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must exist in the graph.")

        index1, index2 = self.nodes[node1], self.nodes[node2]
        self.adj_matrix[index1][index2] = weight
        self.adj_matrix[index2][index1] = weight  # Reflect edge in undirected graph

    def remove_edge(self, node1, node2):
        """Remove the edge between node1 and node2"""
        if node1 in self.nodes and node2 in self.nodes:
            index1, index2 = self.nodes[node1], self.nodes[node2]
            # Edge removal by setting to float('inf')
            self.adj_matrix[index1][index2] = float("inf")
            self.adj_matrix[index2][index1] = float("inf")

    def get_edge_weight(self, node1, node2):
        """Get the weight of the edge between node1 and node2"""
        if node1 in self.nodes and node2 in self.nodes:
            index1, index2 = self.nodes[node1], self.nodes[node2]
            return self.adj_matrix[index1][index2]
        return None

    def __str__(self):
        """String representation of the graph's adjacency matrix"""
        matrix = "\n".join(["\t".join(map(str, row)) for row in self.adj_matrix])
        return f"Adjacency Matrix:\n{matrix}"


if __name__ == "__main__":
    # Usage Examples
    wg = WeightedGraph()
    wg.add_node("A")
    wg.add_node("B")
    wg.add_node("C")

    wg.add_edge("A", "B", 3)
    wg.add_edge("B", "C", 5)
    wg.add_edge("A", "C", 1)

    print(wg)
    print("Weight of the edge between 'A' and 'B':", wg.get_edge_weight("A", "B"))
    print("Weight of the edge between 'B' and 'C':", wg.get_edge_weight("B", "C"))

    wg.remove_edge("A", "C")
    print("\nAfter removing the edge between 'A' and 'C':")
    print(wg)
