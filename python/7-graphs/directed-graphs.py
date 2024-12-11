from collections import deque, defaultdict

class DirectedGraph:
    def __init__(self):
        # Using a dictionary of lists for adjacency representation:
        # graph[u] = [v1, v2, ...] means edges from u to v1, u to v2, etc.
        self.graph = defaultdict(list)

    # Add a node to the graph (optional in Python, as nodes are added implicitly when adding edges)
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add a directed edge from u to v
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Depth-First Search (DFS): Good for exploring paths and detecting cycles
    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)
        print()

    def _dfs_util(self, node, visited):
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self._dfs_util(neighbor, visited)

    # Breadth-First Search (BFS): Good for shortest paths in unweighted graphs
    def bfs(self, start):
        visited = set([start])
        queue = deque([start])

        while queue:
            current = queue.popleft()
            print(current, end=" ")
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    # Print the graph's adjacency list
    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example Usage
if __name__ == "__main__":
    dg = DirectedGraph()
    
    # Adding edges
    dg.add_edge('A', 'B')
    dg.add_edge('A', 'C')
    dg.add_edge('B', 'D')
    dg.add_edge('C', 'D')
    dg.add_edge('C', 'E')

    # Print the adjacency list
    print("Directed Graph Adjacency List:")
    dg.print_graph()

    # Perform DFS
    print("\nDFS starting from 'A':")
    dg.dfs('A')

    # Perform BFS
    print("BFS starting from 'A':")
    dg.bfs('A')