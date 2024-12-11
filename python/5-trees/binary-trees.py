class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a node into the binary tree (level-order)
    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # Preorder traversal (Root -> Left -> Right)
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Inorder traversal (Left -> Root -> Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Postorder traversal (Left -> Right -> Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Level-order traversal (BFS)
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

# Example Usage
if __name__ == "__main__":
    bt = BinaryTree()
    elements = [1, 2, 3, 4, 5, 6, 7]

    for elem in elements:
        bt.insert(elem)

    print("Preorder Traversal:")
    bt.preorder(bt.root)
    print()

    print("Inorder Traversal:")
    bt.inorder(bt.root)
    print()

    print("Postorder Traversal:")
    bt.postorder(bt.root)
    print()

    print("Level-order Traversal:")
    bt.level_order()
    print()