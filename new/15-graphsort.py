import networkx as nx

def graph_sort(graph):
    try:
        # Check if the graph is a directed acyclic graph (DAG)
        if not nx.is_directed_acyclic_graph(graph):
            raise ValueError("The graph must be a directed acyclic graph (DAG).")

        # Perform topological sort
        sorted_nodes = list(nx.topological_sort(graph))

        return sorted_nodes

    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a graph with a cycle
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (2, 3), (3, 4)])

    # Perform graph sort
    result = graph_sort(G)

    print("Graph Sort Result:", result)
