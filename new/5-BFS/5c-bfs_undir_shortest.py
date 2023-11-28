from collections import deque

class SimpleGraph:
    def __init__(self):
        self.nodes = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't already exist."""
        if vertex not in self.nodes:
            self.nodes[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an undirected edge between vertex1 and vertex2."""
        if vertex1 not in self.nodes:
            self.add_vertex(vertex1)
        if vertex2 not in self.nodes:
            self.add_vertex(vertex2)

        self.nodes[vertex1].append(vertex2)
        self.nodes[vertex2].append(vertex1)  # Since the graph is undirected

    def bfs_shortest_path(self, start, end):
        """Perform BFS to compute the shortest path from start to end."""
        if start not in self.nodes or end not in self.nodes:
            return None, []

        visited = set([start])
        queue = deque([(start, 0)])  # Queue stores tuples of (vertex, distance)
        predecessors = {start: None}

        while queue:
            current_vertex, current_distance = queue.popleft()
            if current_vertex == end:
                # Build the shortest path by backtracking through predecessors
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = predecessors[current_vertex]
                path.reverse()  # Reverse the list to get the path from start to end
                return current_distance, path

            # Visit the neighbors
            for neighbor in self.nodes[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    predecessors[neighbor] = current_vertex
                    queue.append((neighbor, current_distance + 1))

        # If BFS completes without finding the end
        return None, []


if __name__ == "__main__":
    # Modified example usage
    simple_graph = SimpleGraph()
    simple_graph.add_edge("X", "Y")
    simple_graph.add_edge("X", "Z")
    simple_graph.add_edge("Y", "W")
    simple_graph.add_edge("Z", "W")
    simple_graph.add_edge("W", "V")
    simple_graph.add_edge("V", "U")

    distance, shortest_path = simple_graph.bfs_shortest_path("X", "U")
    print("Shortest distance: ", distance)
    print("Shortest path: ", shortest_path)
