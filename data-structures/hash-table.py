# Notes
"""
- Store key-value pairs
- Unordered
- Fast for adding, removing, searching values
- Needs a hash function which needs to be fast,
  consistent (same outpu with same input)
Uses
- Storing values
"""


class HashTable:
    def __init__(self, size=53):
        self.key_map = [None] * 53

    def _hash(self, key):
        result = 0
        prime_number = 31

        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            result = (result * prime_number + value) % len(self.key_map)
        return result

    def set(self, key, value):
        index = self._hash(key)

        if not self.key_map[index]:
            self.key_map[index] = []
        self.key_map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)

        if not self.key_map[index]:
            return None

        for item in self.key_map[index]:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):
        keys = []

        for map in self.key_map:
            if map:
                for item in map:
                    keys.append(item[0])
        return keys

    def values(self):
        values = []

        for map in self.key_map:
            if map:
                for item in map:
                    if item[1] not in values:
                        values.append(item[1])
        return values
