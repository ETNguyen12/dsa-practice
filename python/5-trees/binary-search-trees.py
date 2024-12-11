class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    # Search for a value in the BST
    def search(self, value):
        def _search(node, value):
            if not node or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    # Inorder traversal (Left -> Root -> Right)
    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.value, end=" ")
                _inorder(node.right)

        _inorder(self.root)

    # Delete a node from the BST
    def delete(self, value):
        def _delete(node, value):
            if not node:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                # Node with one child or no child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Node with two children
                temp = self._min_value_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)

            return node

        self.root = _delete(self.root, value)

    # Find the minimum value node
    def _min_value_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

# Example Usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]

    for elem in elements:
        bst.insert(elem)

    print("Inorder Traversal:")
    bst.inorder()
    print()

    print("Search for 40:", "Found" if bst.search(40) else "Not Found")
    print("Search for 100:", "Found" if bst.search(100) else "Not Found")

    print("Delete 50 (root):")
    bst.delete(50)
    print("Inorder Traversal After Deletion:")
    bst.inorder()