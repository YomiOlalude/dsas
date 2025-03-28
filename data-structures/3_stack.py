# Notes
"""
Summary
- LIFO
- Stack is more like a concept of LIFO and can be done with
  SLLs, DLLs, arrays, etc
Uses:
- Manages function execution and recursion
- Stores previous states for reverting changes
- Used in calculators and compilers
- Validates code structure
- Manages local variables efficiently
- Undo/Redo
- Browser history
BigO:
- Insertion: O(1)
- Removal: O(1)
- Search: O(n)
- Access(eg. index): O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __repr__(self):
        values = []
        current = self.first

        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def unshift(self, value):
        node = Node(value)

        if not self.first:
            self.first = node
            self.last = self.first
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        return self.size + 1

    def shift(self):
        if not self.first:
            return False

        if self.first == self.last:
            self.last = None

        node = self.first
        self.first = self.first.next
        self.size -= 1
        return node.value
