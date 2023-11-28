def topological_sort(graph):
    UNVISITED, VISITING, VISITED = 0, 1, 2  # States for DFS: unvisited, visiting, visited
    topological_order = []  # List to store the topological order
    has_cycle = False  # Flag to detect a cycle

    # Initial state: all vertices are unvisited (UNVISITED)
    state = {node: UNVISITED for node in graph}

    def dfs(node):
        nonlocal has_cycle
        if has_cycle:  # If a cycle is found, we stop further DFS
            return
        state[node] = VISITING  # Mark the node as visiting (VISITING)
        for neighbor in graph[node]:
            if state[neighbor] == VISITING:  # A back-edge found, hence a cycle exists
                has_cycle = True
                return
            if state[neighbor] == UNVISITED:  # If unvisited, perform DFS
                dfs(neighbor)
        state[node] = VISITED  # Mark the node as visited (VISITED)
        topological_order.append(node)  # Add node to the topological order

    for node in graph:
        if state[node] == UNVISITED:  # Perform DFS only on unvisited nodes
            dfs(node)
        if has_cycle:  # Stop if a cycle is detected
            break

    if has_cycle:
        print("The graph has a cycle, therefore no topological ordering is possible.")
    else:
        # The order is reversed since vertices are added at the end of the process
        topological_order.reverse()
        print("The topological ordering of the graph is:")
        print(topological_order)


if __name__ == "__main__":
    # Example usage with a graph as an adjacency list
    graph_without_cycles = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }

    print("Graph without cycles:")
    topological_sort(graph_without_cycles)

    print("\nGraph with a cycle:")
    graph_with_cycle = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }
    topological_sort(graph_with_cycle)

