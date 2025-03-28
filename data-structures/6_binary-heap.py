# Notes
"""
- A heap is a special kind of binary tree that satisfies the heap property
- Each parent has at most 2 child nodes
- The value of each parent node is always greater than
  its child nodes in max binary heap
- In min binary heap, the parent node is always less than the children
- No order to sibling nodes
- Left children are filled out first
- For any index n of an array, the left child is stored at 2n + 1
  and the right child is stored at 2n + 2
- For any index n of an array, the parent is at (n - 1) // 2
Uses:
- Used to implement priority queues
Big O:
- Insertion: O(log n)
- Removal: O(log n)
- Search: O(n)
"""

import heapq


class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)
        self.bubble_up()

    def remove_max(self):
        highest = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.bubble_down()
        return highest

    def bubble_up(self):
        """
        fix at correct position
        """
        index = len(self.values) - 1
        node = self.values[index]

        while True:
            parent_index = index - 1 // 2
            parent = self.values[parent_index]

            if node <= parent:
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

                if left_child > node:
                    swap = left_child_index

            if right_child_index < len(self.values):
                right_child = self.values[right_child_index]

                if (not swap and right_child > node) or (
                    swap and right_child > left_child
                ):
                    swap = right_child_index

            if not swap:
                break

            self.values[index] = self.values[swap]
            self.values[swap] = node
            index = swap


# Heaps with native Python module

# Min Binary Heap
min_heap = []

heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 5)

# Max Binary Heap
# 1: Use the negative value
max_heap1 = []

heapq.heappush(max_heap1, -11)
heapq.heappush(max_heap1, -7)
heapq.heappush(max_heap1, -3)
heapq.heappush(max_heap1, -8)
heapq.heappush(max_heap1, -10)
heapq.heappush(max_heap1, -6)

print(-heapq.heappop(max_heap1))  # prints largest value

# 2: Use a tuple with negative priorities
max_heap2 = []

heapq.heappush(max_heap2, (-5, 5))
heapq.heappush(max_heap2, (-1, 1))
heapq.heappush(max_heap2, (-2, 2))
heapq.heappush(max_heap2, (-4, 4))
heapq.heappush(max_heap2, (-3, 3))
heapq.heappush(max_heap2, (-6, 6))

print(max_heap2[0])  # prints largest value's tuple
print(heapq.heappop(max_heap2)[1])  # prints largest value

# Build a heap from an existing list
heap_arr = [5, 4, 3, 2, 1]

heapq.heapify(heap_arr)
