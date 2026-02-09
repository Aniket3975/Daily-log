# Hash Map Implementation in Python

class Node:
    # Each node will hold a key-value pair
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # Initialize the hash map with a size of 10 slots
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size

    # Hash function to calculate the index for a given key
    def _hash(self, key):
        return hash(key) % self.size

    # Insert or update a value in the hash map
    def insert(self, key, value):
        index = self._hash(key)
        node = self.slots[index]

        if not node:
            self.slots[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    # Get the value associated with a given key from the hash map
    def get(self, key):
        index = self._hash(key)
        node = self.slots[index]

        if not node:
            return None
        elif node.key == key:
            return node.value
        else:
            while node.next:
                node = node.next
                if node.key == key:
                    return node.value
            return None

    # Remove a value from the hash map with a given key
    def remove(self, key):
        index = self._hash(key)
        node = self.slots[index]

        if not node:
            return
        elif node.key == key:
            self.slots[index] = node.next
            return

        prev_node = None
        while node and node.next:
            if node.next.key == key:
                prev_node.next = node.next.next
                break
            else:
                prev_node = node
                node = node.next

    # Display the contents of the hash map
    def display(self):
        for index, slot in enumerate(self.slots):
            print(f"Slot {index}: ", end="")
            while slot:
                print(f"[{slot.key} -> {slot.value}]", end=" ")
                slot = slot.next
            print()

# Example usage of the hash map
hash_map = HashMap()
hash_map.insert("John", 25)
hash_map.insert("Alice", 30)
hash_map.insert("Bob", 35)

print("Hash Map Contents:")
hash_map.display()

print("\nGet value for John:", hash_map.get("John"))
print("Get value for Alice:", hash_map.get("Alice"))

hash_map.remove("John")

print("\nHash Map Contents after removal:")
hash_map.display()