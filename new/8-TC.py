import numpy as np

class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)

    def add_edge(self, source, destination):
        self.adj_matrix[source][destination] = 1

    def print_graph(self):
        print("Original Graph:")
        for vertex in range(self.vertices):
            neighbors = [str(i) for i in range(self.vertices) if self.adj_matrix[vertex][i] == 1]
            print(f"{vertex} -> {neighbors}")

    def print_transitive_closure(self):
        transitive_closure_matrix = self.compute_transitive_closure()
        print("\nTransitive Closure:")
        for vertex in range(self.vertices):
            closure_set = set(np.where(transitive_closure_matrix[vertex] == 1)[0])
            print(f"{vertex} -> {closure_set}")

    def compute_transitive_closure(self):
        T = np.copy(self.adj_matrix)

        changed = True
        while changed:
            temp = np.copy(T)
            T = np.logical_or(T, np.dot(T, T))
            changed = not np.array_equal(T, temp)

        return T

if __name__ == "__main__":
    # Example usage
    graph = DirectedGraph(4)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 2)
    graph.add_edge(3, 3)

    graph.print_graph()
    graph.print_transitive_closure()
