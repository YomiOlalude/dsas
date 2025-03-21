# Notes
"""
- Used where elements need to be processed in order of priority
- A data structure where each element has a priority
- Elements with higher priority are served before elements with
  lower priority
- It's more like a concept, can be done with heaps or least, but
  it's better with heaps for better performance
Uses:
- Task scheduling
"""


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.values.append(node)
        self.bubble_up()

    def dequeue(self):
        lowest = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.bubble_down()
        return lowest.value

    def bubble_up(self):
        """
        fix at correct position
        """
        index = len(self.values) - 1
        node = self.values[index]

        while True:
            parent_index = (index - 1) // 2
            parent = self.values[parent_index]

            if node.priority >= parent.priority:
                break
            self.values[parent_index] = node
            self.values[index] = parent
            index = parent_index

    def bubble_down(self):
        index = 0
        node = self.values[0]

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            swap = None

            if left_child_index < len(self.values):
                left_child = self.values[left_child_index]

                if left_child.priority < node.priority:
                    swap = left_child_index

            if right_child_index < len(self.values):
                right_child = self.values[right_child_index]

                if (not swap and right_child.priority < node.priority) or (
                    swap and right_child.priority < left_child.priority
                ):
                    swap = right_child_index

            if not swap:
                break

            self.values[index] = self.values[swap]
            self.values[swap] = node
            index = swap
