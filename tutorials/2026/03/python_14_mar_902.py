# Trie Data Structure in Python
=====================================

This code implements the basic operations of a Trie data structure.

```python
class Node:
    # Each node in the trie has a dictionary to store its children and a boolean to mark the end of a word.
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    # The trie is implemented as a class with methods for insertion, search, and deletion.
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        # Start at the root node and traverse down to the final character of the word.
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        
        # Mark the end of the word.
        current_node.end_of_word = True

    def search(self, word):
        # Start at the root node and traverse down to the final character of the word.
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False  # Word not found.
            current_node = current_node.children[char]
        
        # Return True if the end of the word is marked, False otherwise.
        return current_node.end_of_word

    def delete(self, word):
        # Start at the root node and traverse down to the final character of the word.
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return  # Word not found.
            current_node = current_node.children[char]
        
        # If the end of the word is marked, delete it. Otherwise, remove the node from its parent's children.
        if current_node.end_of_word:
            self._delete_node(current_node)
        else:
            self._remove_from_parent(current_node)

    def _delete_node(self, node):
        # Remove a node and all nodes below it that do not have any children.
        for char in list(node.children.keys()):
            child = node.children[char]
            if len(child.children) == 0:
                del node.children[char]
            else:
                self._delete_node(child)

    def _remove_from_parent(self, node):
        # Remove a node from its parent's children.
        parent = node.parent
        if parent in node.children:
            del node.children[parent]

# Example usage
trie = Trie()
words = ['hello', 'world', 'hell', 'word']

for word in words:
    trie.insert(word)

print(trie.search('hello'))  # True
print(trie.search('world'))  # True
print(trie.search('hell'))   # True
print(trie.search('word'))   # True
print(trie.search('foo'))    # False

trie.delete('hello')
print(trie.search('hello'))  # False