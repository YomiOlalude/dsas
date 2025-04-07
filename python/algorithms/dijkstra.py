# Notes
"""
- One of the most famous and widely used algorithms
- Finds the shortest path between 2 vertices on a graph
- Figures out the fastest way to get from point A to B
- Implemented using a Weighted Graph
- Need to understand Graphs and Priority Queues first
Uses:
- Google maps
- Public transport system
- Telecommunication
- Airline tickets
- Network routing
- Anything where determining shortest path is important
"""

from dataclasses import dataclass
from math import inf


@dataclass
class WeightedVertex:
    vertex: str
    weight: int


class WeightedGraph:
    """
    Steps
    - Every time we look to visit a new vertex, we pick the vertex with the smallest known distance
      to visit first (which starts with itself with distance of 0)
    - Once we've moved to the vertex we're going to visit, we look at each of its neighbors
    - For each neighboring vertex, we calculate the distance by summing the total edges that lead to
      the vertex we're checking from the starting vertex
    - If the new total distance to a vertex is less than the previous total, we store the new shorter
      distance for that vertex
    Pseudocode
    1. This function should accept a starting and ending vertex
    2. Create an object (distances) and set each key to be every vertex in the adjacency list with a
       value of infinity, except for the starting vertex which should have a value of 0
    3. After setting a value in the distances object, add each vertex with a weight of infinity to
       to the weight queue, except the starting vertex, which should have a weight of 0 because
       that's where we begin
    4. Create another object called previous and set each key to be every vertex in the adjacency list
       with a value of None
    5. Start looping as long as there is anything in the weight queue
       - dequeue a vertex from the weight queue
       - if that vertex is the same as the ending vertex - we are done
       - otherwise loop through each value in the adjacency list at that vertex
            • calculate the distance to that vertex from the starting vertex
            • if the distance is less than what is currently stored in our distances object,
                - update the distances object with new lower distance
                - update the previous object to contain that vertex
                - enqueue the vertex with the total distance from the start vertex
    """

    def __init__(self):
        self.adjacency_list: dict[str, list[WeightedVertex]] = {}
        self.ordered_vertices_queue: list[WeightedVertex] = []

    def __enqueue(self, vertex: str, weight: int):
        self.ordered_vertices_queue.append({"vertex": vertex, "weight": weight})
        self.ordered_vertices_queue.sort(key=lambda vertex: vertex["weight"])
        return self.ordered_vertices_queue

    def add_vertex(self, vertex: str):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        return self.adjacency_list

    def add_edge(self, vertex1: str, vertex2: str, weight: int):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise KeyError("Error with vertices keys")

        self.adjacency_list[vertex1].append({"vertex": vertex2, "weight": weight})
        self.adjacency_list[vertex2].append({"vertex": vertex1, "weight": weight})
        return True

    def dijkstra(self, start: str, end: str):
        # stores the vertices current shortest path to get to a vertix e.g {vertex2: vertex1, vertex3}
        shortest_path_mapping = {}
        # stores the vertices current shortest distance to get to a vertix e.g {vertex2: vertex1, 3}
        distances = {}
        result = []

        # build initial state
        """
        distances = {vertex1: 0, vertex2: inf, vertex3: inf}
        previous = {vertex1: None, vertex2: None, vertex3: None}
        """
        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                self.__enqueue(vertex, 0)
            else:
                distances[vertex] = inf
                self.__enqueue(vertex, inf)
            shortest_path_mapping[vertex] = None

        # as long as there's something to visit
        while self.ordered_vertices_queue:
            smallest_vertex = self.ordered_vertices_queue.pop(0)["vertex"]

            # end of process
            if smallest_vertex == end:
                while shortest_path_mapping[smallest_vertex]:
                    result.append(smallest_vertex)
                    smallest_vertex = shortest_path_mapping[smallest_vertex]
                break

            if smallest_vertex:
                for neighbor in self.adjacency_list[smallest_vertex]:
                    # calculate new distance to neighboring vertex
                    new_distance = distances[smallest_vertex] + neighbor["weight"]
                    neighbor_vertex = neighbor["vertex"]

                    if new_distance < distances[neighbor_vertex]:
                        # updating new smallest_vertex distance to neighbor
                        distances[neighbor_vertex] = new_distance
                        # updating previous - How we got to the neighbor
                        shortest_path_mapping[neighbor_vertex] = smallest_vertex
                        # enqueue in weight queue with new weight
                        self.__enqueue(neighbor_vertex, new_distance)
        result.reverse()
        return [start] + result


wg = WeightedGraph()

wg.add_vertex("A")
wg.add_vertex("B")
wg.add_vertex("C")
wg.add_vertex("D")
wg.add_vertex("E")
wg.add_vertex("F")

wg.add_edge("A", "B", 4)
wg.add_edge("A", "C", 2)
wg.add_edge("B", "E", 3)
wg.add_edge("C", "D", 2)
wg.add_edge("C", "F", 4)
wg.add_edge("D", "E", 3)
wg.add_edge("D", "F", 1)
wg.add_edge("E", "F", 1)


print(wg.dijkstra("A", "E"))
