# Notes
"""
Summary
- Great for insertion and deletion (better than arrays) at the beginning
- No indeces like arrays
Uses:
- Enables moving forward and backward between visited pages
- Used in text editors, graphic design tools, and IDEs
- Supports previous and next track navigation
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
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        values = []
        current = self.head

        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values)

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.length += 1
            self.tail = self.head
            return self

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None

        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None

        self.length -= 1
        return node

    def shift(self):
        if not self.head:
            return None

        node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        self.length -= 1
        return node

    def unshift(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index <= self.length // 2:
            current = self.head
            counter = 0

            while counter != index:
                current = current.next
                counter += 1
        else:
            current = self.tail
            counter = self.length - 1

            while counter != index:
                current = current.prev
                counter -= 1

        return current

    def set(self, index, value):
        node = self.get(index)

        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.unshift(value)

        if index == self.length:
            return self.append(value)

        node = Node(value)

        found_node = self.get(index)
        prev_found_node = found_node.prev

        prev_found_node.next = node
        node.prev = prev_found_node

        node.next = found_node
        found_node.prev = node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index it out of range")

        if index == 0:
            return self.shift()

        if index == self.length - 1:
            return self.pop()

        node = self.get(index)

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None

        self.length -= 1
        return True
