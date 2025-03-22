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
import math


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append({"value": value, "priority": priority})
        self.values.sort(key=lambda item: item["priority"])

    def dequeue(self):
        return self.values.pop(0)


class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        return self.adjacency_list

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise KeyError("Key error with vertices")

        self.adjacency_list[vertex1].append({"node": vertex2, "weight": weight})
        self.adjacency_list[vertex2].append({"node": vertex1, "weight": weight})
        return True

    def dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []

        # build initial state
        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = math.inf
                nodes.enqueue(vertex, math.inf)
            previous[vertex] = None

        # as long as there's something to visit
        while nodes.values:
            smallest = nodes.dequeue()["value"]

            if smallest == finish:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                break

            if smallest or distances[smallest] != math.inf:
                for neighbor in self.adjacency_list[smallest]:
                    # Find neighboring node
                    next_node = neighbor
                    # Calculate new distance to neighboring node
                    candidate = distances[smallest] + next_node["weight"]
                    next_neighbor = next_node["node"]

                    if candidate < distances[next_neighbor]:
                        # Updating new smallest distance to neighbor
                        distances[next_neighbor] = candidate
                        # Updating previous - How we got to the neighbor
                        previous[next_neighbor] = smallest
                        # Enqueue in priority queue with new priority
                        nodes.enqueue(next_neighbor, candidate)

        path.reverse()
        return [smallest] + path
