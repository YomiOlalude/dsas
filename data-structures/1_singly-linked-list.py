# Notes
"""
Summary
- Great for insertion and deletion (better than arrays) at the beginning
- No indeces like arrays
Uses:
- Implementing a music playlist (next song navigation)
- Browser tabs (storing open tabs in order)
- Low-level memory management (dynamic memory allocation)
- Undo feature in applications (storing previous states)
- Managing a queue of print jobs in a printer spooler
BigO:
- Insertion: O(1)
- Removal: O(1) or O(n)
- Search: O(n)
- Access(eg. index): O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
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
        return " -> ".join(values)

    def __str__(self):
        result = ""
        current = self.head

        while current:
            if current.next:
                result += str(current.value) + " -> "
            else:
                result += str(current.value)
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = self.head

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def append2(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return self

        current = self.head

        while current.next:
            current = current.next

        current.next = node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None

        current = self.head
        new_tail = current

        while current.next:
            new_tail = current
            current = current.next

        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        if not self.head:
            return None

        current_head = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return current_head

    def unshift(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = self.head

        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def get(self, index):
        if index > self.length or index < 0:
            return IndexError("Index it out of range")

        if index == 0:
            return self.head

        current = self.head
        counter = 0

        while counter != index:
            current = current.next
            counter += 1
        return current

    def set(self, index, value):
        node = self.get(index)

        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return IndexError("Index it out of range")

        if index == self.length:
            return self.append(value)

        if index == 0:
            return self.unshift(value)

        new_node = Node(value)
        prev = self.get(index - 1)
        current = prev.next
        prev.next = new_node
        new_node.next = current
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return IndexError("Index it out of range")

        if index == 0:
            return self.shift()
        prev = self.get(index - 1)
        next_node = self.get(index + 1)

        prev.next = next_node
        self.length -= 1
        return self

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return True

    def insert_in_middle(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return self

        slow = self.head
        fast = self.head
        prev = False

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        node.next = prev.next
        prev.next = node
        return self

    def insert_in_middle2(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return self

        middle = self.length // 2
        prev = self.get(middle)

        prev_next = prev.next
        prev.next = node
        node.next = prev_next
        self.length += 1
        return self
