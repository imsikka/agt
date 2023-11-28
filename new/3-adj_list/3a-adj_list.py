class UndirectedGraphAdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Add a new node to the graph if it doesn't already exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        """Add an edge between node1 and node2."""
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)

        # Add the edge for an undirected graph
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def remove_edge(self, node1, node2):
        """Remove the edge between node1 and node2."""
        if node1 in self.adj_list and node2 in self.adj_list[node1]:
            self.adj_list[node1].remove(node2)
        if node2 in self.adj_list and node1 in self.adj_list[node2]:
            self.adj_list[node2].remove(node1)

    def has_edge(self, node1, node2):
        """Check if there is an edge between node1 and node2."""
        if node1 in self.adj_list:
            return node2 in self.adj_list[node1]
        return False

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(
            f"{node}: {neighbors}" for node, neighbors in self.adj_list.items()
        )


if __name__ == "__main__":
    # Usage Examples
    graph = UndirectedGraphAdjacencyList()
    graph.add_node(1)
    graph.add_node("A")
    graph.add_node("B")

    graph.add_edge(1, "A")
    graph.add_edge("A", "B")

    print(graph)
    print("Does an edge exist between 1 and 'A'? ", graph.has_edge(1, "A"))
    print("Does an edge exist between 'A' and 'B'? ", graph.has_edge("A", "B"))
    print("Does an edge exist between 1 and 'B'? ", graph.has_edge(1, "B"))

    graph.remove_edge("A", "B")
    print("\nAfter removing the edge between 'A' and 'B':")
    print(graph)
