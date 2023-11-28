class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        """Adds a node to the graph if it doesn't exist."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node, to_node):
        """Adds a directed edge from 'from_node' to 'to_node'."""
        self.add_node(from_node)
        self.add_node(to_node)
        self.adj_list[from_node].append(to_node)

    def dfs(self, source=None):
        """Performs DFS from the specified source node."""
        if source is None:
            source = next(iter(self.adj_list), None)  # Default to first node if exists

        if source is None:
            raise ValueError("Graph is empty, cannot perform DFS.")

        visit_number = 1
        completion_number = 0
        visited = set()
        stack = [(source, iter(self.adj_list[source]))]  # Stack of (node, iterator over neighbors)
        dfs_visit_numbers = {source: visit_number}
        dfs_completion_numbers = {}

        visit_number += 1
        while stack:
            node, neighbors = stack[-1]

            if node not in visited:
                visited.add(node)
                dfs_completion_numbers[node] = completion_number
                completion_number += 1

            try:
                # Visit unvisited neighbors
                neighbor = next(neighbors)
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs_visit_numbers[neighbor] = visit_number
                    visit_number += 1
                    stack.append((neighbor, iter(self.adj_list[neighbor])))
            except StopIteration:
                # If all neighbors visited, pop node from stack
                stack.pop()

        return dfs_visit_numbers, dfs_completion_numbers

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())


if __name__ == "__main__":
    # Example usage:
    graph = DirectedGraph()
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
