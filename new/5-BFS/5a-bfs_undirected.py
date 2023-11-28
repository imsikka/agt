from collections import deque

class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        for node in [node1, node2]:
            if node not in self.adjacency_list:
                self.add_node(node)
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def bfs(self, source=None):
        if source is None:
            source = next(iter(self.adjacency_list))
        visited_nodes = set()
        visit_order = {}
        completion_order = {}
        visit_number = 1

        queue = deque([(source, None)])  # Queue with nodes and their predecessors

        while queue:
            current_node, predecessor = queue.popleft()
            if current_node not in visited_nodes:
                visited_nodes.add(current_node)
                visit_order[current_node] = visit_number
                visit_number += 1
                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited_nodes:
                        queue.append((neighbor, current_node))

        for completion_number, node in enumerate(visited_nodes, start=1):
            completion_order[node] = completion_number

        return visit_order, completion_order

if __name__ == "__main__":
    graph = UndirectedGraph()

    # Creating a different graph structure
    graph.add_node("X")
    graph.add_node("Y")
    graph.add_node("Z")
    graph.add_edge("X", "Y")
    graph.add_edge("Y", "Z")
    graph.add_edge("Z", "X")

    # Adding disconnected nodes
    graph.add_node("W")
    graph.add_node("K")

    bfs_visit, bfs_complete = graph.bfs(source="X")
    print("BFS visitation numbers:", bfs_visit)
    print("BFS completion numbers:", bfs_complete)

    bfs_visit, bfs_complete = graph.bfs(source="W")
    print("BFS visitation numbers (from W):", bfs_visit)
    print("BFS completion numbers (from W):", bfs_complete)


