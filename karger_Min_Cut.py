import random
import copy
from collections import defaultdict


# Load and parse the graph from file
def load_graph(filepath):
    graph = defaultdict(list)
    with open(filepath, 'r') as file:
        for line in file:
            parts = list(map(int, line.strip().split()))
            vertex = parts[0]
            edges = parts[1:]
            graph[vertex].extend(edges)
    return graph


# Karger's randomized contraction algorithm
def karger_min_cut(original_graph):
    graph = copy.deepcopy(original_graph)

    while len(graph) > 2:
        # Randomly pick an edge (u, v)
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # Merge v into u
        graph[u].extend(graph[v])

        # Replace all occurrences of v with u
        for vertex in graph[v]:
            graph[vertex] = [u if x == v else x for x in graph[vertex]]

        # Remove self-loops
        graph[u] = [x for x in graph[u] if x != u]

        # Remove vertex v from graph
        del graph[v]

    # Return number of crossing edges between final two vertices
    remaining_vertices = list(graph.keys())
    return len(graph[remaining_vertices[0]])


# Run the algorithm multiple times to increase chance of getting min cut
if __name__ == "__main__":
    graph_path = "karger_Min_Cut.txt"  # Replace with full path if needed
    original_graph = load_graph(graph_path)

    min_cut = float('inf')
    for _ in range(100):  # You can increase this number for better reliability
        cut = karger_min_cut(original_graph)
        if cut < min_cut:
            min_cut = cut

    print("Minimum cut found:", min_cut)
