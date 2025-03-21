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
