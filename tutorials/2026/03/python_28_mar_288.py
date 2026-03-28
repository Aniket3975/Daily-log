# Hash Map Implementation in Python

class Node:
    # Node class represents individual elements of the hash map
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    # HashMap class represents the hash map data structure
    def __init__(self, size):
        """
        Initialize a new HashMap with the given size.

        :param size: The initial capacity of the hash map.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        # Calculate the index for the given key using a simple hash function
        return hash(key) % self.size


    def put(self, key, value):
        """
        Add or update a key-value pair in the hash map.

        :param key: The key to be added or updated.
        :param value: The corresponding value.
        """
        index = self._hash(key)
        node = self.table[index]

        # Check if the key already exists
        while node:
            if node.key == key:
                node.value = value  # Update the existing value
                return
            node = node.next

        # Create a new node and add it to the table
        node = Node(key, value)
        node.next = self.table[index]
        self.table[index] = node


    def get(self, key):
        """
        Retrieve the value associated with a given key.

        :param key: The key for which to retrieve the value.
        :return: The corresponding value if found; otherwise None.
        """
        index = self._hash(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value  # Return the associated value
            node = node.next

        return None


    def remove(self, key):
        """
        Remove a key-value pair from the hash map.

        :param key: The key to be removed.
        """
        index = self._hash(key)
        node = self.table[index]
        prev_node = None

        while node:
            if node.key == key:
                # Handle the case when the key is at the end of the linked list
                if not node.next:
                    self.table[index] = None
                    return

                # Remove the node from the table and its predecessor
                prev_node.next = node.next
                return
            prev_node = node
            node = node.next


    def display(self):
        """
        Print the contents of the hash map.
        """
        for index, node in enumerate(self.table):
            print(f"Index {index}: ", end="")
            while node:
                print(f"[{node.key}={node.value}], ", end="")
                node = node.next
            print()


# Example usage
if __name__ == "__main__":
    # Create a new hash map with an initial capacity of 10
    hash_map = HashMap(10)

    # Add some key-value pairs to the hash map
    hash_map.put("apple", "fruit")
    hash_map.put("banana", "fruit")
    hash_map.put("carrot", "vegetable")

    # Retrieve values from the hash map
    print(hash_map.get("apple"))  # Output: fruit
    print(hash_map.get("banana"))