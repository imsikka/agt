from collections import deque

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        """Add a node to the graph if it doesn't already exist."""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, from_node, to_node):
        """Add a directed edge from from_node to to_node."""
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_list[from_node].append(to_node)

    def bfs(self, source=None):
        """Perform breadth-first search starting from the specified source node."""
        if source is None:
            # Default source node is the first in the adjacency list
            source = next(iter(self.adjacency_list))
        
        visit_number = 1
        bfs_visit_numbers = {}
        bfs_completion_numbers = {}
        visited = set()
        queue = deque([(source, None)])  # Queue with nodes and their predecessors

        while queue:
            current_node, predecessor = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                bfs_visit_numbers[current_node] = visit_number
                queue.extend(
                    (neighbor, current_node)
                    for neighbor in self.adjacency_list[current_node]
                    if neighbor not in visited
                )
                visit_number += 1

        # After the BFS, set the completion number
        for completion_number, node in enumerate(visited, start=1):
            bfs_completion_numbers[node] = completion_number

        return bfs_visit_numbers, bfs_completion_numbers

    def __str__(self):
        """String representation of the graph's adjacency list."""
        return "\n".join(
            f"{node}: {neighbors}" for node, neighbors in self.adjacency_list.items()
        )

if __name__ == "__main__":
    # Example usage:
    graph = DirectedGraph()
    # Creating nodes and directed edges
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")
    graph.add_edge("E", "A")
    graph.add_edge("A", "D")
    graph.add_edge("B", "E")
    
    bfs_visit, bfs_complete = graph.bfs(source="A")
    print("BFS visitation numbers:", bfs_visit)
    print("BFS completion numbers:", bfs_complete)

    # Perform BFS from another node
    bfs_visit, bfs_complete = graph.bfs(source="C")
    print("BFS visitation numbers (from C):", bfs_visit)
    print("BFS completion numbers (from C):", bfs_complete)

