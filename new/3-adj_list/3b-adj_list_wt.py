class UndirectedWeightedGraphAdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Add a new node to the graph if it doesn't already exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2, weight):
        """Add an undirected, weighted edge between node1 and node2."""
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)

        # Ensure edge doesn't exist before adding it
        if not self.has_edge(node1, node2):
            self.adj_list[node1].append((node2, weight))
            self.adj_list[node2].append((node1, weight))

    def remove_edge(self, node1, node2):
        """Remove the undirected edge between node1 and node2."""
        if node1 in self.adj_list:
            self.adj_list[node1] = [
                (neighbor, weight)
                for neighbor, weight in self.adj_list[node1]
                if neighbor != node2
            ]
        if node2 in self.adj_list:
            self.adj_list[node2] = [
                (neighbor, weight)
                for neighbor, weight in self.adj_list[node2]
                if neighbor != node1
            ]

    def has_edge(self, node1, node2):
        """Check if there is an edge between node1 and node2."""
        if node1 in self.adj_list:
            for neighbor, _ in self.adj_list[node1]:
                if neighbor == node2:
                    return True
        return False

    def __str__(self):
        """String representation of the graph's adjacency list."""
        graph_str = []
        for node, neighbors in self.adj_list.items():
            edges = ", ".join(f"{n} (weight: {w})" for n, w in neighbors)
            graph_str.append(f"{node}: {edges}")
        return "\n".join(graph_str)


if __name__ == "__main__":
    # Usage Examples
    weighted_graph = UndirectedWeightedGraphAdjacencyList()
    weighted_graph.add_node(1)
    weighted_graph.add_node("A")
    weighted_graph.add_node("B")

    weighted_graph.add_edge(1, "A", 3)
    weighted_graph.add_edge("A", "B", 5)
    weighted_graph.add_edge(1, "B", 8)

    print(weighted_graph)
    print("Does an edge exist between 1 and 'A'? ", weighted_graph.has_edge(1, "A"))
    print("Does an edge exist between 'A' and 'B'? ", weighted_graph.has_edge("A", "B"))
    print("Does an edge exist between 1 and 'B'? ", weighted_graph.has_edge(1, "B"))

    weighted_graph.remove_edge("A", "B")
    print("\nAfter removing the edge between 'A' and 'B':")
    print(weighted_graph)
