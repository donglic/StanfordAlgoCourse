from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices=0):
        self.graph = defaultdict(list)
        self.V = vertices

    # Use this method to populate the graph from a .txt file
    def populated_graph_from_file(self, filename):
        vertex_set = set()

        # read the edges from buffer line by line
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 2:
                    continue  # Skip malformed lines
                tail, head = map(int, parts)
                self.graph[tail].append(head)

                # Track both vertices
                vertex_set.add(tail)
                vertex_set.add(head)
        self.V = len(vertex_set)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # get G_rev by reversing all edges
    def _transpose(self):
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def dfs_output_finish_time_queue(self, start, step, node_color_status, finish_time_heap):
        stack = [start]
        while stack:
            step += 1
            v = stack[-1]  # peek top of stack
            if node_color_status[v - 1]:  # if the node has been seen before
                v = stack.pop()  # pop it from stack
                if node_color_status[v - 1] == 1:  # if Gray, finish exploring
                    heapq.heappush(finish_time_heap, (-step, v))
                    node_color_status[v - 1] = 2  # Black, indicate finish exploring
            else:  # seen the node for the first time
                node_color_status[v - 1] = 1  # Gray, indicate the node has been discovered
                for w in self.graph[v]:
                    if not node_color_status[w - 1]:
                        stack.append(w)

    def fill_order(self, node_color_status, finish_time_heap):
        # 0 = whiter, 1 = grey, 2 = black
        step = 0
        for node in range(self.V, 0, -1):  # Ensure reverse order traversal
            curr_node_status = node_color_status[node-1]
            if not curr_node_status:
                self.dfs_output_finish_time_queue(node, step, node_color_status, finish_time_heap)

    # Iterative DFS function
    def dfs_populate_cc(self, start, node_color_status, component):
        """

        :param start: starting node
        :param node_color_status: list to keep track node exploration status
        :param component: list of a connected component
        """
        stack = [start]
        while stack:
            v = stack[-1]  # peek top of stack
            if node_color_status[v - 1]:  # if the node has been seen before
                v = stack.pop()  # pop it from stack
                if node_color_status[v - 1] == 1:  # if Gray, finish exploring
                    node_color_status[v - 1] = 2  # Black, indicate finish exploring
            else:  # seen the node for the first time
                node_color_status[v - 1] = 1  # Gray, indicate the node has been discovered
                component.append(v)
                for w in self.graph[v]:
                    if not node_color_status[w - 1]:
                        stack.append(w)

    def kosaraju_top_k_scc(self, k):
        node_status = [0] * self.V
        finish_time_max_heap = []
        transposed_graph = self._transpose()
        transposed_graph.fill_order(node_status, finish_time_max_heap)
        node_status = [0] * self.V
        scc_list = []

        while finish_time_max_heap:
            _, curr_node = heapq.heappop(finish_time_max_heap)
            curr_node_status = node_status[curr_node-1]
            if not curr_node_status:
                component = []
                self.dfs_populate_cc(curr_node, node_status, component)
                scc_list.append(component)

        # Sort by descending size and take top-k
        scc_list.sort(key=len, reverse=True)
        return scc_list[:k]

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.populated_graph_from_file("SCC.txt")

    sccs = g.kosaraju_top_k_scc(5)
    for scc in sccs:
        print(len(scc))
    #print("Strongly Connected Components:", sccs)


