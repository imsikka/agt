class DirectedWeightedGraphAdjacencyList:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Add a node to the graph if it doesn't already exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node, to_node, weight):
        """Add a directed, weighted edge from `from_node` to `to_node`."""
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        # Add the edge with its weight
        self.adj_list[from_node].append((to_node, weight))

    def remove_edge(self, from_node, to_node):
        """Remove the directed edge from `from_node` to `to_node`."""
        if from_node in self.adj_list:
            self.adj_list[from_node] = [
                (target, weight)
                for target, weight in self.adj_list[from_node]
                if target != to_node
            ]

    def get_edge_weight(self, from_node, to_node):
        """Get the weight of an edge from `from_node` to `to_node`."""
        if from_node in self.adj_list:
            for target, weight in self.adj_list[from_node]:
                if target == to_node:
                    return weight
        return None

    def has_edge(self, from_node, to_node):
        """Check if there is a directed edge from `from_node` to `to_node`."""
        if from_node in self.adj_list:
            return any(to_node == target for target, _ in self.adj_list[from_node])
        return False

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(
            [
                f"{node}: {', '.join(f'{target} (weight: {weight})' for target, weight in neighbors)}"
                for node, neighbors in self.adj_list.items()
            ]
        )


if __name__ == "__main__":
    # Usage examples
    dw_graph = DirectedWeightedGraphAdjacencyList()
    dw_graph.add_node(1)
    dw_graph.add_node("A")
    dw_graph.add_node("B")

    dw_graph.add_edge(1, "A", 3)
    dw_graph.add_edge("A", "B", 5)
    dw_graph.add_edge("B", 1, 2)

    print(dw_graph)
    print("Does an edge exist from 1 to 'A'? ", dw_graph.has_edge(1, "A"))
    print("Does an edge exist from 'A' to 1? ", dw_graph.has_edge("A", 1))
    print("Does an edge exist from 'A' to 'B'? ", dw_graph.has_edge("A", "B"))

    print("Weight from 1 to 'A':", dw_graph.get_edge_weight(1, "A"))
    print("Weight from 'A' to 'B':", dw_graph.get_edge_weight("A", "B"))

    dw_graph.remove_edge("A", "B")
    print("\nAfter removing the edge from 'A' to 'B':")
    print(dw_graph)
