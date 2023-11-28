from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_connected_components(self):
        vertices = list(self.graph.keys())
        visited = {v: False for v in vertices}
        components = 0

        for vertex in vertices:
            if not visited[vertex]:
                self.dfs(vertex, visited)
                components += 1

        return components

# Example Usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)

num_components = g.count_connected_components()
print("Number of connected components:", num_components)
