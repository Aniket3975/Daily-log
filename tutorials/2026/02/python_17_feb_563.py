# Tree Traversal Algorithms
=====================================

This script teaches three fundamental tree traversal algorithms: Inorder, Preorder, and Postorder traversals.
These algorithms are used to traverse or search through a binary tree data structure.

```python
class Node:
    def __init__(self, value):
        # Initialize the node with a given value
        self.value = value
        # Set left and right children as None initially
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Performs an Inorder traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree.
    
    Returns:
        list: A list of values in the order they are visited.
    """
    # Initialize a list to store the visited values
    visited = []
    
    # Define a recursive helper function for Inorder traversal
    def traverse(node):
        if node is not None:
            # Recursively visit the left subtree first
            traverse(node.left)
            # Visit the current node and append its value to the visited list
            visited.append(node.value)
            # Then, recursively visit the right subtree
            traverse(node.right)
    
    # Start the traversal from the root node
    traverse(root)
    return visited

def preorder_traversal(root):
    """
    Performs a Preorder traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree.
    
    Returns:
        list: A list of values in the order they are visited.
    """
    # Initialize a list to store the visited values
    visited = []
    
    # Define a recursive helper function for Preorder traversal
    def traverse(node):
        if node is not None:
            # Visit the current node and append its value to the visited list
            visited.append(node.value)
            # Recursively visit the left subtree first
            traverse(node.left)
            # Then, recursively visit the right subtree
            traverse(node.right)
    
    # Start the traversal from the root node
    traverse(root)
    return visited

def postorder_traversal(root):
    """
    Performs a Postorder traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree.
    
    Returns:
        list: A list of values in the order they are visited.
    """
    # Initialize a list to store the visited values
    visited = []
    
    # Define a recursive helper function for Postorder traversal
    def traverse(node):
        if node is not None:
            # Recursively visit the left subtree first
            traverse(node.left)
            # Then, recursively visit the right subtree
            traverse(node.right)
            # Visit the current node and append its value to the visited list
            visited.append(node.value)
    
    # Start the traversal from the root node
    traverse(root)
    return visited

# Example usage:
if __name__ == "__main__":
    # Create a binary tree for testing
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal:", inorder_traversal(root))
    print("Preorder traversal:", preorder_traversal(root))
    print("Postorder traversal:", postorder_traversal(root))