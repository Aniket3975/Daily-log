# Hash Map Implementation in Python
```python
class Node:
    # Define the structure of a node in the hash map
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # Initialize the hash map with a given size
    def __init__(self, size=10):
        self.size = size
        self.map = [None] * size

    # Function to handle collisions by chaining
    def _hash_function(self, key):
        return hash(key) % self.size

    # Method to add or update a key-value pair in the hash map
    def set(self, key, value):
        index = self._hash_function(key)
        
        if self.map[index] is None:
            self.map[index] = Node(key, value)
        else:
            node = self.map[index]
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    # Method to retrieve a value from the hash map based on a given key
    def get(self, key):
        index = self._hash_function(key)
        
        if self.map[index] is None:
            return None
        else:
            node = self.map[index]
            while node:
                if node.key == key:
                    return node.value
                node = node.next

# Example usage of the hash map implementation
if __name__ == "__main__":
    hash_map = HashMap()
    
    # Add some key-value pairs to the hash map
    hash_map.set("apple", 5)
    hash_map.set("banana", 10)
    hash_map.set("orange", 15)

    # Retrieve values from the hash map using keys
    print(hash_map.get("apple"))  # Output: 5
    print(hash_map.get("banana"))  # Output: 10
    print(hash_map.get("orange"))  # Output: 15
    
    # Update a value in the hash map using its key
    hash_map.set("banana", 20)
    print(hash_map.get("banana"))  # Output: 20