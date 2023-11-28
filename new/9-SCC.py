from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def dfs_scc(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_scc(i, visited, result)

    def get_scc(self):
        stack = []
        visited = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        gr = self.transpose()

        visited = [False] * (self.V)
        scc_list = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                result = []
                gr.dfs_scc(i, visited, result)
                scc_list.append(result)

        return scc_list

# Example usage:
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
scc_result = g.get_scc()
for component in scc_result:
    print(component)
