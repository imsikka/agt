class DirectedGraphAdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Add a node to the graph if it doesn't already exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node, to_node):
        """Add a directed edge from `from_node` to `to_node`."""
        # Ensure both nodes exist in the graph
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        # Add to_node to the adjacency list of from_node
        self.adj_list[from_node].append(to_node)

    def remove_edge(self, from_node, to_node):
        """Remove the directed edge from `from_node` to `to_node`."""
        if from_node in self.adj_list and to_node in self.adj_list[from_node]:
            self.adj_list[from_node].remove(to_node)

    def has_edge(self, from_node, to_node):
        """Check if there is a directed edge from `from_node` to `to_node`."""
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(
            f"{node}: {neighbors}" for node, neighbors in self.adj_list.items()
        )


if __name__ == "__main__":
    # Usage examples
    directed_graph = DirectedGraphAdjacencyList()
    directed_graph.add_node(1)
    directed_graph.add_node("A")
    directed_graph.add_node("B")

    directed_graph.add_edge(1, "A")
    directed_graph.add_edge("A", "B")
    directed_graph.add_edge("B", 1)  # Adding a cycle for demonstration

    print(directed_graph)
    print("Does an edge exist from 1 to 'A'? ", directed_graph.has_edge(1, "A"))
    print("Does an edge exist from 'A' to 1? ", directed_graph.has_edge("A", 1))
    print("Does an edge exist from 'A' to 'B'? ", directed_graph.has_edge("A", "B"))

    directed_graph.remove_edge("A", "B")
    print("\nAfter removing the edge from 'A' to 'B':")
    print(directed_graph)
