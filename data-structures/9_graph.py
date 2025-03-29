# Notes
"""
- Collection of nodes
Graph Terms
- Vertex: node
- Edge: connection between nodes
- Weighted - eg. Google maps with distance as the weight value
- Unweighted: eg. Facebook friends, no value on edges
- Undirected graph: No direction between vertices eg. Facebook friends
- Directed graph: Direction/arrows between vertices eg. X followers
- Adjacency list can be like the:
 {
  "A": ["B", "C"],
  "B": ["A", "D"]
  }
  or
 [
  [1, 2, 3],
  [3, 4, 5],
 ]
Uses:
- GPS Navigation (Shortest Path)
- Recommender System (Netflix, Amazon, Spotify)
- Social Network (Friend Suggestions)
- AWS Neptune DB
- Location/Mapping
"""


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        return self.adjacency_list

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise KeyError("Key error with vertices")

        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise KeyError("Key error with vertices")

        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return KeyError("Key error with vertex")

        for edge in self.adjacency_list[vertex]:
            self.adjacency_list[edge].remove(vertex)
        del self.adjacency_list[vertex]
        return self.adjacency_list

    def depth_first_traversal_recursive(self, start_vertex):
        """
        Traversal uses
        - web crawlers
        - peer to peer networking
        - shortest path problems
        - solving mazes
        - matches/rcommendations
        """
        result = []
        visited = {}

        def dfs(vertex):
            if vertex in visited:
                return None
            visited[vertex] = True
            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return result

    def depth_first_traversal_iterative(self, start_vertex):
        stack = [start_vertex]
        result = []
        visited = {}

        visited[start_vertex] = True

        while len(stack):
            current_vertex = stack.pop()
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return result

    def breadth_first_traversal(self, start_vertex):
        queue = [start_vertex]
        result = []
        visited = {}

        visited[start_vertex] = True

        while len(queue):
            current_vertex = queue.pop(0)
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result
