class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Ensures that the node is in the adjacency list."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def dfs(self, source=None):
        """Performs DFS from the specified source node."""
        if source is None:
            source = next(iter(self.adj_list))  # Default to first node

        visit_number = 1
        completion_number = 0
        visited = set()
        stack = [
            (source, iter(self.adj_list[source]))
        ]  # Stack of tuples (node, iterator over neighbors)
        dfs_visit_numbers = {source: visit_number}
        parents = {source: None}
        dfs_completion_numbers = {}

        visit_number += 1
        while stack:
            node, neighbors = stack[-1]
            visited.add(node)

            try:
                # Visit unvisited neighbors
                neighbor = next(neighbors)
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs_visit_numbers[neighbor] = visit_number
                    parents[neighbor] = node  # Track parent
                    visit_number += 1
                    stack.append((neighbor, iter(self.adj_list[neighbor])))
            except StopIteration:
                # If all neighbors visited, pop node from stack & set completion number
                stack.pop()
                completion_number += 1
                dfs_completion_numbers[node] = completion_number

        return dfs_visit_numbers, dfs_completion_numbers, parents

    def classify_edges(self, dfs_visit_numbers, dfs_completion_numbers, parents):
        edge_types = {}

        for u in dfs_visit_numbers.keys():
            for v in self.adj_list[u]:
                if parents[v] == u:  # Tree edge: v is a child of u
                    edge_types[(u, v)] = "Tree Edge"
                elif v in dfs_visit_numbers:
                    if (dfs_visit_numbers[u] < dfs_visit_numbers[v]) and (
                        dfs_completion_numbers[u] > dfs_completion_numbers[v]
                    ):
                        edge_types[(u, v)] = "Forward Edge"

        # Reversed tree and forward edges are back edges
        edge_types_ = {}
        for u, v in edge_types:
            edge_types_[(v, u)] = "Back Edge"
        edge_types.update(edge_types_)

        return edge_types

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(
            f"{node}: {neighbors}" for node, neighbors in self.adj_list.items()
        )


if __name__ == "__main__":
    # Example usage:
    graph = UndirectedGraph()
    graph.add_node(1)
    graph.add_node("A")
    graph.add_edge(1, "A")
    graph.add_edge("A", "B")
    graph.add_edge(2, "B")
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(3, "C")  # Disconnected component

    visited_order, completion_order, parents = graph.dfs(source=1)
    print("DFS Visitation Order:", visited_order)
    print("DFS Completion Order:", completion_order)

    print("Edge types:", graph.classify_edges(*graph.dfs(source=1)))
