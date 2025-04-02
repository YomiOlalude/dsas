# Notes
"""
- Type of tree
- Data structure for storing items (usually strings) based off of prefixes the items share in common
Uses:
- Word search
"""


class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def add_word(self, word):
        current = self.root

        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current["*"] = "*"

    def does_word_exist(self, word):
        current = self.root

        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return "*" in current
