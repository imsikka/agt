from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BCCUtil(self, u, parent, low, disc, stackMember, st):
        children = 0
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                parent[v] = u
                children += 1
                self.BCCUtil(v, parent, low, disc, stackMember, st)

                low[u] = min(low[u], low[v])

                if (
                    parent[u] == -1
                    and children > 1
                    or parent[u] != -1
                    and low[v] >= disc[u]
                ):
                    w = -1
                    bcc = []
                    while w != u:
                        w = st.pop()
                        bcc.append(w)
                        stackMember[w] = False
                    print(f"BCC: {bcc}")
            elif v != parent[u] and stackMember[v] is True:
                low[u] = min(low[u], disc[v])

    def BCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        stackMember = [False] * self.V
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.BCCUtil(i, parent, low, disc, stackMember, st)

            if stackMember[i] is True:
                remaining_vertices = []
                while st:
                    w = st.pop()
                    remaining_vertices.append(w)
                    stackMember[w] = False
                if remaining_vertices:
                    print(f"BCC: {remaining_vertices}")


# Example execution
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    print("Bi-Connected Components in the given graph are:")
    g.BCC()
