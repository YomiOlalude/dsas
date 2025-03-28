# Notes
# Tree
"""
Summary
- Root: top node in the tree
- Child: a node directly connected to another node down the tree
- Parent: the converse notion of a child
- Sibling: node with the same parent
- Leaf: node with no children
- Edge: the connection between one node and another
Uses:
- Organize directories and files in a hierarchical structure
- Used in indexing for efficient searching
- Represents document structure in web browsers - HTML DOM
- Used in IP routing and autocomplete features
- Used for machine learning and game AI
- Parses code into an abstract syntax tree (AST)
- Used in network routing and optimization
- Used for data compression
- JSON
"""

# BST
"""
Summary
- Every parent has at most 2 children
- Children are sorted from left to right
- Every node to the left is always smaller than the parent
- Every node to the right is always greater than the parent
- No duplicates
Uses:
- Searching
BigO:
- Insertion: O(log n)
- Search: O(log n)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def view(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            if node.right:
                self.view(node.right, level + 1, "R--> ")
            print("   " * level + prefix + str(node.value))
            if node.left:
                self.view(node.left, level + 1, "L--> ")

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return self

        current = self.root

        while True:
            if value == current.value:
                return False

            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                else:
                    current = current.left

            if value > current.value:
                if not current.right:
                    current.right = node
                    return self
                else:
                    current = current.right

    def find(self, value):
        if not self.root:
            return None

        current = self.root
        found = False

        while current and not found:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True

        if not found:
            return False
        return True

    def bfs(self):
        """
        breadth first search: returns all values searching breadth first
        """
        queue = []
        result = []
        current = self.root

        queue.append(self.root)

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def dfs_preorder(self):
        """
        - depth first search preorder
        - root gets added first
        - reverse of dfs_postorder
        """

        result = []
        current = self.root

        def traverse(node):
            result.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(current)
        return result

    def dfs_postorder(self):
        """
        - depth first search postorder
        - root gets added last
        - reverse of dfs_preorder
        """

        result = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.value)

        traverse(current)
        return result

    def dfs_inorder(self):
        """
        - depth first search inorder
        - traverses left side first
        - list ends up in order
        """

        result = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(current)
        return result
