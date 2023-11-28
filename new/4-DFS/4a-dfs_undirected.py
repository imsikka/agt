from collections import defaultdict

class UndirectedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node]

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def dfs(self, source=None):
        """Performs DFS from the specified source node."""
        if source is None:
            source = next(iter(self.adj_list))  # Default to first node

        visited_order = {}
        completion_order = {}
        visit_number = 1
        completion_number = 0

        def dfs_visit(node):
            nonlocal visit_number, completion_number
            visited_order[node] = visit_number
            visit_number += 1

            for neighbor in self.adj_list[node]:
                if neighbor not in visited_order:
                    dfs_visit(neighbor)

            completion_number += 1
            completion_order[node] = completion_number

        dfs_visit(source)
        return visited_order, completion_order

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())


if __name__ == "__main__":
    # Example usage:
    graph = UndirectedGraph()
    graph.add_node(1)
    graph.add_node("A")
    graph.add_edge(1, "A")
    graph.add_edge("A", "B")
    graph.add_edge(2, "B")
    graph.add_edge(1, 2)
    graph.add_edge(3, "C")  # Disconnected component

    visited_order, completion_order = graph.dfs(source=1)
    print("DFS Visitation Order:", visited_order)
    print("DFS Completion Order:", completion_order)

    # Perform DFS from the other component
    visited_order, completion_order = graph.dfs(source=3)
    print("DFS Visitation Order (from 3):", visited_order)
    print("DFS Completion Order (from 3):", completion_order)
