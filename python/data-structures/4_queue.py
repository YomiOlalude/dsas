# Notes
"""
Summary
- FIFO
Uses:
- Message brokers like RabbitMQ, Kafka, and AWS SQS use
  queues to handle async communication
- Web servers queue incoming requests before processing them
- Customer service calls are queued in FIFO order
BigO:
- Insertion: O(1)
- Removal: O(1)
- Search: O(n)
- Access(eg. index): O(n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = 0


class Queue:
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

    def enqueue(self, value):
        node = Node(value)

        if not self.first:
            self.first = node
            self.last = self.first
        else:
            last = self.last
            last.next = node
            self.last = node
        return self.size + 1

    def dequeue(self):
        if not self.first:
            return False

        if self.first == self.last:
            self.last = None

        node = self.first
        self.first = self.first.next
        self.size -= 1
        return node.value
