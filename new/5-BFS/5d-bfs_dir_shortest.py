from collections import deque

class DirectedSimpleGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph if it doesn't already exist."""
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex):
        """Add a directed edge from from_vertex to to_vertex."""
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex].append(to_vertex)

    def bfs_shortest_path(self, start, end):
        """Perform BFS to compute the shortest path from start to end."""
        if start not in self.vertices or end not in self.vertices:
            return None, []

        visited = set([start])
        queue = deque([(start, 0)])  # Queue stores tuples of (vertex, distance)
        predecessors = {start: None}

        while queue:
            current_vertex, current_distance = queue.popleft()
            if current_vertex == end:
                # Build shortest path from start to end by backtracking
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = predecessors[current_vertex]
                path.reverse()  # Path constructed in reverse from end to start
                return current_distance, path

            # Visit the neighbors
            for neighbor in self.vertices[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    predecessors[neighbor] = current_vertex
                    queue.append((neighbor, current_distance + 1))

        # If BFS completes without finding the end
        return None, []


# Modified example usage
if __name__ == "__main__":
    directed_simple_graph = DirectedSimpleGraph()
    directed_simple_graph.add_directed_edge("X", "Y")
    directed_simple_graph.add_directed_edge("X", "Z")
    directed_simple_graph.add_directed_edge("Y", "W")
    directed_simple_graph.add_directed_edge("Z", "W")
    directed_simple_graph.add_directed_edge("W", "V")
    directed_simple_graph.add_directed_edge("V", "U")

    distance, shortest_path = directed_simple_graph.bfs_shortest_path("X", "U")
    print("Shortest distance: ", distance)
    print("Shortest path: ", shortest_path)
