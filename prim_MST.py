import heapq
from collections import defaultdict

def read_graph(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    num_nodes, num_edges = map(int, lines[0].strip().split())
    graph = defaultdict(list)
    for line in lines[1:]:
        u, v, cost = map(int, line.strip().split())
        graph[u].append((cost, v))
        graph[v].append((cost, u))  # Undirected graph
    return graph, num_nodes

def prim_mst(graph, num_nodes):
    visited = set()
    min_heap = [(0, 1)]  # Start from node 1
    total_cost = 0

    while len(visited) < num_nodes:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        for edge_cost, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_cost, v))

    return total_cost

if __name__ == "__main__":
    filepath = "edges.txt"
    graph, num_nodes = read_graph(filepath)
    mst_cost = prim_mst(graph, num_nodes)
    print(f"Total cost of the MST: {mst_cost:,}")
